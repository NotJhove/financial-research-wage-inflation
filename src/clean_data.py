import pandas as pd


# Load raw datasets
cpi_data = pd.read_csv("data/raw/cpi_raw.csv")
wage_data = pd.read_csv("data/raw/wages_raw.csv")


# Convert dates to datetime
cpi_data["observation_date"] = pd.to_datetime(
    cpi_data["observation_date"]
)

wage_data["observation_date"] = pd.to_datetime(
    wage_data["observation_date"]
)


# Calculate year-over-year inflation
# Uses the CPI value from 12 months earlier.
cpi_data["inflation_yoy"] = (
    cpi_data["CPIAUCSL"].pct_change(periods=12) * 100
)


# Calculate year-over-year wage growth
# Uses the wage value from 12 months earlier.
wage_data["wage_growth_yoy"] = (
    wage_data["AHETPI"].pct_change(periods=12) * 100
)


# Keep observations from January 2020 onward.
# The YoY calculations are performed before filtering
# so that the 2020 values can use the previous year's data.
cpi_data = cpi_data[
    cpi_data["observation_date"] >= "2020-01-01"
]

wage_data = wage_data[
    wage_data["observation_date"] >= "2020-01-01"
]


# Save processed datasets
cpi_data.to_csv(
    "data/processed/cpi_processed.csv",
    index=False
)

wage_data.to_csv(
    "data/processed/wages_processed.csv",
    index=False
)


print("Processed data saved successfully.")