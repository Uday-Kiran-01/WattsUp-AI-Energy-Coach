# src/utils/config.py
import os

RAW_DATA_PATH = os.path.join("data", "raw", "household_power_consumption.txt")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "processed_data.csv")
SYNTHETIC_DATA_PATH = os.path.join("data", "synthetic", "synthetic_households.csv")

OUTPUT_DIR = "outputs"
MODEL_DIR = os.path.join(OUTPUT_DIR, "models")
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")
REPORTS_DIR = os.path.join(OUTPUT_DIR, "reports")

N_CLUSTERS = 3