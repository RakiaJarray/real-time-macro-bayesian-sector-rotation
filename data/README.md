# Data

This directory contains the datasets used in this research project.

## Raw Data

Original datasets downloaded from external sources. They must remain unchanged.

### FRED-MD

Monthly macroeconomic time series and historical real-time vintages.

Source: https://www.stlouisfed.org/research/economists/mccracken/fred-databases

Directory: `raw/fred_md/`

### Sector Returns

Monthly returns of the 12 industry portfolios.

Source: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

Directory: `raw/sector_returns/`

## Processed Data

- `processed/macro/`: Cleaned macroeconomic variables.
- `processed/sectors/`: Prepared sector returns.
- `processed/merged/`: Aligned macroeconomic and sector datasets.

## Data Management Principles

- Preserve original datasets.
- Record download dates and data vintages.
- Avoid look-ahead bias.
- Use only information available at each observation date.
- Document preprocessing transformations.
