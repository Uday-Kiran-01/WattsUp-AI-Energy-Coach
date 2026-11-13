# Data Guide

This project expects data to be arranged under the `data/` directory with the following conventions:

- `data/raw/` — raw input files (do not modify original files if you want reproducibility)
- `data/processed/` — cleaned and transformed datasets used for modeling and feature building
- `data/synthetic/` — generated synthetic datasets used for testing and experimentation

Example dataset: `household_power_consumption.txt`

Typical columns (UCI household power consumption format):

- `Date` — date string (e.g., `16/12/2006`)
- `Time` — time string (e.g., `17:24:00`)
- `Global_active_power` — household global active power (kilowatts)
- `Global_reactive_power`
- `Voltage`
- `Global_intensity`
- `Sub_metering_1`, `Sub_metering_2`, `Sub_metering_3`

Best practices

- Keep raw files intact and write cleaning scripts to read from `data/raw/` and write to `data/processed/`.
- Document any transformations applied in `md/DATA.md` or in preprocessing scripts in `src/data/`.
- For large datasets, store the canonical copy in a remote object store and place small samples in `data/raw/`.
