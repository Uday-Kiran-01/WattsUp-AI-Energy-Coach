# # main.py
# import os
# import pandas as pd

# from src.data.load_data import load_raw_data
# from src.data.preprocess import preprocess_data
# from src.data.simulate_household import generate_synthetic_households
# from src.features.build_features import build_forecast_features
# from src.forecasting.forecast_model import train_forecast_model, evaluate_model
# from src.segmentation.cluster_customers import cluster_households
# from src.recommendations.recommend import get_recommendations
# from src.genai.explain import explain_customer
# from src.utils.config import OUTPUT_DIR

# def main():
#     print("Loading raw data...")
#     raw_path = os.path.join("data", "raw", "household_power_consumption.txt")
#     df = load_raw_data(raw_path)

#     print("Preprocessing...")
#     df = preprocess_data(df)

#     print("Generating synthetic households...")
#     synthetic_df = generate_synthetic_households(df, n_customers=50)

#     print("Feature engineering (forecasting on base data)...")
#     X, y = build_forecast_features(df)

#     # Temporal train-test split (train on first 80% days, test on last 20%)
#     split_idx = int(len(X) * 0.8)
#     X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
#     y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

#     print("Training forecasting model...")
#     model = train_forecast_model(X_train, y_train)
#     metrics = evaluate_model(model, X_test, y_test)
#     print(f"Forecast Metrics: {metrics}")

#     print("Aggregating households for clustering...")
#     household_summary = synthetic_df.groupby("household_id").agg({
#         "consumption_kwh": ["mean", "max", "min"]
#     })
#     household_summary.columns = ["mean_kwh", "max_kwh", "min_kwh"]

#     print("Clustering households...")
#     household_summary = cluster_households(household_summary)

#     print("Generating customer reports...\n")
#     for idx, row in household_summary.iterrows():
#         recs = get_recommendations(row["cluster"])
#         explanation = explain_customer(
#             household=row,
#             recommendations=recs,
#             metrics=metrics
#         )
#         print(f"Customer {idx} Report:\n")
#         print(explanation)
#         print("-" * 50)

# if __name__ == "__main__":
#     os.makedirs(OUTPUT_DIR, exist_ok=True)
#     main()

from src.data.load_data import load_uci_data
from src.data.preprocess import preprocess_data
from src.data.synthetic import generate_synthetic_households
from src.features.build_features import add_lag_features
from src.forecasting.forecast_model import train_forecast_model, evaluate_model
from src.segmentation.cluster_customers import cluster_households
from src.recommendation.recommend import get_recommendations
from src.genai.explain import generate_customer_explanation
from src.utils import config

import pandas as pd

def main():
    # ------------------------------
    # 1. Load & preprocess data
    # ------------------------------
    print("Loading data...")
    df = load_uci_data(config.RAW_DATA_PATH)

    print("Preprocessing...")
    df = preprocess_data(df)  # ensure datetime index

    # ------------------------------
    # 2. Generate synthetic households
    # ------------------------------
    print("Generating synthetic households...")
    synthetic_df = generate_synthetic_households(df, n_households=50)

    # Ensure datetime column for synthetic data
    if "datetime" not in synthetic_df.columns and "date" in synthetic_df.columns:
        synthetic_df["datetime"] = pd.to_datetime(synthetic_df["date"])

    # ------------------------------
    # 3. Feature engineering (forecasting)
    # ------------------------------
    print("Feature engineering...")
    df_feat = add_lag_features(df)

    X = df_feat[["lag_1", "lag_2", "lag_7", "rolling_7d_mean", "day_of_week"]]
    y = df_feat["Global_active_power"]

    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # ------------------------------
    # 4. Forecasting
    # ------------------------------
    print("Training forecasting model...")
    model = train_forecast_model(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)
    print("Forecast Metrics:", metrics)

    # ------------------------------
    # 5. Aggregate households for clustering
    # ------------------------------
    print("Aggregating households for clustering...")
    agg = synthetic_df.groupby("household_id")["consumption"].agg([
        "mean", "max", "std"
    ])

    # ------------------------------
    # 5b. Quarterly/Seasonal Analysis
    # ------------------------------
    print("Quarterly/Seasonal Analysis:")
    synthetic_df["quarter"] = synthetic_df["datetime"].dt.to_period("Q")
    quarterly = synthetic_df.groupby(["household_id", "quarter"])['consumption'].mean().reset_index()
    for hid in quarterly["household_id"].unique():
        qdata = quarterly[quarterly["household_id"] == hid]
        print(f"Household {hid} quarterly average kWh:")
        for _, row in qdata.iterrows():
            print(f"  Quarter {row['quarter']}: {row['consumption']:.2f} kWh/day")
        print()

    # ------------------------------
    # 5c. Peak Detection & Duration
    # ------------------------------
    print("Peak Detection & Duration:")
    # Work household-by-household on a downsampled slice to avoid huge
    # intermediate arrays while still capturing peak patterns.
    for hid in synthetic_df["household_id"].unique():
        group = synthetic_df[synthetic_df["household_id"] == hid].copy()
        group = group.sort_values("datetime")

        # Downsample: take every 60th point (approx hourly if data is minutely)
        group = group.iloc[::60, :]
        if group.empty:
            continue

        threshold = group["consumption"].quantile(0.8)
        peaks = group[group["consumption"] > threshold]
        n_peaks = len(peaks)

        group["is_peak"] = group["consumption"] > threshold
        group["peak_block"] = (group["is_peak"] != group["is_peak"].shift()).cumsum()
        peak_durations = group[group["is_peak"]].groupby("peak_block").size().tolist()

        if group["datetime"].dt.hour.nunique() > 1:
            group["hour"] = group["datetime"].dt.hour
            tod_peaks = group[group["is_peak"]]["hour"].value_counts().sort_index()
        else:
            tod_peaks = None

        print(f"Household {hid}:")
        print(f"  Number of peaks: {n_peaks}")
        print(f"  Peak durations (sampled time-steps): {peak_durations}")
        if tod_peaks is not None:
            print("  Time-of-day peak counts:")
            for hour, count in tod_peaks.items():
                print(f"    Hour {hour}: {count}")
        print()

    # ------------------------------
    # 5d. Voltage/Safety Insights
    # ------------------------------
    print("Voltage/Safety Insights:")
    if "Voltage" in synthetic_df.columns:
        for hid, group in synthetic_df.groupby("household_id"):
            n_abnormal = ((group["Voltage"] < 220) | (group["Voltage"] > 250)).sum()
            if n_abnormal > 0:
                print(f"Household {hid}: {n_abnormal} hours outside safe voltage range (220–250V). Consider checking wiring or contacting your utility provider.")
            else:
                print(f"Household {hid}: All voltage readings within safe range.")
    else:
        print("Voltage data not available in synthetic_df.")

    # Enrich aggregation with variability metrics
    agg["peak_ratio"] = agg["max"] / agg["mean"]
    agg["variability"] = agg["std"] / agg["mean"]

    print("Clustering households...")
    agg = cluster_households(agg, n_clusters=config.N_CLUSTERS)

    # ------------------------------
    # 6. Generate customer reports
    # ------------------------------
    print("Generating customer reports...\n")
    avg_consumption = agg["mean"].mean()
    for idx, row in agg.iterrows():
        recs, kwh_savings, cost_savings, co2_savings = get_recommendations({
            "cluster": row["cluster"],
            "kWh": row["mean"]
        })

        report = generate_customer_explanation(
            consumption=row["mean"],
            avg=avg_consumption,
            cluster=row["cluster"],
            recommendations=recs,
            kwh_savings=kwh_savings,
            cost_savings=cost_savings,
            co2_savings=co2_savings
        )

        print(f"Customer {idx} Report:")
        print(report)
        print("-" * 50)


if __name__ == "__main__":
    main()