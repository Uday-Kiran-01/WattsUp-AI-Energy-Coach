# Usage

This document contains more detailed setup and run instructions than the top-level README.

Environment setup

```bash
# create virtual environment
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

Running the app

- Start the Streamlit demo:

```bash
streamlit run app/streamlit_app.py
```

- Run the demo entrypoint (if present):

```bash
python main.py
```

Common developer tasks

- Build features:

```bash
python -m src.features.build_features
```

- Run data preprocessing:

```bash
python -m src.data.preprocess
```

- Train or run forecasting (script may accept CLI args):

```bash
python -m src.forecasting.forecast_model
```

Inspecting outputs

- Processed datasets: `data/processed/`
- Model artifacts: `outputs/models/`
- Plots and reports: `outputs/plots/` `outputs/reports/`

If you need help running a specific module, open an issue with the command you tried and any error output.
