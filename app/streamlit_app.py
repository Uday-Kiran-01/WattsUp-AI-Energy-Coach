import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="WattsUp AI Energy Coach", layout="wide")
st.title("WattsUp: AI Energy Coach Dashboard")

# Load processed/synthetic data
data_path = os.path.join("data", "synthetic", "synthetic_households.csv")
if os.path.exists(data_path):
    df = pd.read_csv(data_path, parse_dates=["date"])
    st.success("Synthetic household data loaded.")
else:
    st.error("Synthetic household data not found. Run the main pipeline first.")
    st.stop()

# Sidebar: Household selection
household_ids = df["household_id"].unique()
hid = st.sidebar.selectbox("Select Household", household_ids)
house = df[df["household_id"] == hid]

# Show age profile
if "age_profile" in house.columns:
    st.sidebar.markdown(f"**Age Profile:** {house['age_profile'].iloc[0]}")

# Plot daily consumption
daily = house.set_index("date").resample("D")["consumption"].sum()
st.subheader("Daily Consumption (kWh)")
st.line_chart(daily)

# Quarterly/seasonal analysis
house["quarter"] = house["date"].dt.to_period("Q")
quarterly = house.groupby("quarter")["consumption"].mean()
st.subheader("Quarterly Average Consumption (kWh/day)")
st.bar_chart(quarterly)

# Peak detection
threshold = house["consumption"].quantile(0.8)
peaks = house[house["consumption"] > threshold]
st.subheader("Peak Usage Analysis")
st.write(f"80th percentile threshold: {threshold:.2f} kWh")
st.write(f"Number of peaks: {len(peaks)}")

# Voltage safety (if available)
if "Voltage" in house.columns:
    n_abnormal = ((house["Voltage"] < 220) | (house["Voltage"] > 250)).sum()
    st.subheader("Voltage Safety")
    if n_abnormal > 0:
        st.warning(f"{n_abnormal} hours outside safe voltage range (220–250V)")
    else:
        st.success("All voltage readings within safe range.")

# Cluster info (if available)
if "cluster" in house.columns:
    st.sidebar.markdown(f"**Cluster:** {house['cluster'].iloc[0]}")

# Recommendations (placeholder)
st.subheader("Personalized Recommendations")
st.write("See main pipeline output for detailed recommendations and impact metrics.")
