# WattsUp-AI-Energy-Coach

A small Python project for household energy forecasting and recommendations.

## Overview

This repository contains code and data for building, forecasting, and recommending energy-saving actions for households. It includes data processing, feature engineering, forecasting models, segmentation, and a simple Streamlit app for demonstration.

## Quick Start

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or PowerShell/CMD
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit demo (if installed):

```bash
# Option A: run the top-level entrypoint
python main.py

# Option B: run Streamlit app directly
streamlit run app/streamlit_app.py
```

## Project Structure

- `main.py` – project entrypoint for demos
- `app/streamlit_app.py` – Streamlit user interface
- `data/` – raw and processed datasets
- `src/` – project source code
  - `src/data/` – loaders and preprocessing
  - `src/features/` – feature building (e.g., `build_features.py`)
  - `src/forecasting/` – forecasting models
  - `src/recommendation/` – recommendation logic
  - `src/segmentation/` – clustering and segmentation
  - `src/genai/` – explainability helpers
  - `src/utils/` – config and plotting helpers

## Data

Place raw data in `data/raw/` and processed outputs will appear in `data/processed/`. A provided sample dataset is `data/raw/household_power_consumption.txt`.

## Documentation

More detailed project docs live in the `md/` folder:

- `md/ARCHITECTURE.md` — architecture overview and data flow
- `md/USAGE.md` — detailed setup and run commands
- `md/DATA.md` — data layout and expected formats
- `md/MODELS.md` — model locations and artifact guidance
- `md/CONTRIBUTING.md` — contributing and development workflow

## Development Notes

- Tests: no tests included by default. Add `pytest` and test modules under `tests/`.
- Linting / formatting: consider `black` and `ruff` for consistent style.

## Contributing

Open an issue or pull request for bug fixes and improvements.

## License

This project is unlicensed. Add a license file if you intend to share publicly.
