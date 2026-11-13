# Architecture Overview

This document explains the high-level structure of the project and where responsibilities live.

Components

- `data/` – storage for raw and processed data. Raw data is the single source of truth; processing produces cleaned, feature-ready datasets.
- `src/data/` – ETL utilities: loading, cleaning, and synthetic data generation (`load_data.py`, `preprocess.py`, `synthetic.py`).
- `src/features/` – feature engineering: time-based features, rolling windows, aggregations, and feature export (`build_features.py`).
- `src/forecasting/` – forecasting model code and training/inference utilities (`forecast_model.py`).
- `src/segmentation/` – customer clustering and segmentation logic (`cluster_customers.py`).
- `src/recommendation/` – recommendation generation using model outputs (`recommend.py`).
- `src/genai/` – explainability and natural-language explanations (`explain.py`).
- `src/utils/` – configuration, plotting helpers, and common utilities (`config.py`, `plot_utils.py`).

Data flow

1. Raw data is placed in `data/raw/` (e.g., `household_power_consumption.txt`).
2. Data loaders in `src/data/` read and clean the raw files and write outputs to `data/processed/`.
3. Feature builder (`src/features/build_features.py`) consumes processed data and writes feature tables to `data/processed/` or `outputs/`.
4. Forecasting models are trained using feature tables and model artifacts are saved to `outputs/models/`.
5. Recommendation and explainability components read model outputs and generate user-facing content or reports in `outputs/reports/`.

Storage and artifacts

- Processed datasets: `data/processed/`
- Model artifacts: `outputs/models/`
- Plots and reports: `outputs/plots/`, `outputs/reports/`

Notes

- Keep large data and model artifacts out of version control. Use the `outputs/` and `data/` folders for local storage or link to remote storage for production.
