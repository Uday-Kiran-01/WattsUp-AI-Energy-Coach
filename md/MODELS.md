# Models

This document describes where model code lives and how model artifacts are organized.

Where code lives

- Model training and inference logic is under `src/forecasting/` (see `forecast_model.py`).

Model artifacts

- Trained models and checkpoints are stored in `outputs/models/`.
- For reproducibility, include model configuration (hyperparameters, feature list, training dates) alongside saved artifacts.

Common model types you might find or add

- Classical time-series: SARIMA, Exponential Smoothing
- Tree-based regressors: `sklearn`'s RandomForest, GradientBoosting
- Neural methods: simple LSTM or seq2seq models for multi-step forecasting
- Probabilistic models: Prophet or probabilistic deep models

Training and evaluation

- Implement training loops in `src/forecasting/` and save metrics to `outputs/plots/` or `outputs/reports/`.
- When adding a new model, create an entry in `md/MODELS.md` documenting:
  - input features
  - training command or script
  - saved artifact format and location
