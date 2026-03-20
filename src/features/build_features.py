# # src/features/build_features.py
# def create_features(df):
#     """
#     Build lag & day-of-week features for forecasting.
#     """
#     df = df.copy()
#     df['lag1'] = df['kWh'].shift(1).fillna(method='bfill')
#     df['dow'] = df['datetime'].dt.dayofweek
#     X = df[['lag1', 'dow']]
#     y = df['kWh']
#     return X, y

# src/features/build_features.py
import pandas as pd

def add_lag_features(df):
    df = df.copy()
    df["lag_1"] = df["Global_active_power"].shift(1)
    df["lag_2"] = df["Global_active_power"].shift(2)
    df["lag_7"] = df["Global_active_power"].shift(7)

    # 7-day rolling mean
    df["rolling_7d_mean"] = df["Global_active_power"].rolling(window=7).mean()

    # Day of week (0=Monday, 6=Sunday)
    df["day_of_week"] = df["datetime"].dt.dayofweek

    # Fill NA from shifts/rolling
    df.fillna(method="bfill", inplace=True)

    return df