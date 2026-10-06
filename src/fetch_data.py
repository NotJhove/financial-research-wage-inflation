import pandas as pd


# FRED data sources
CPI_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL"
WAGE_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=AHETPI"


# Load data from FRED
cpi_data = pd.read_csv(CPI_URL)
wage_data = pd.read_csv(WAGE_URL)


# Display a quick preview
print("CPI data:")
print(cpi_data.head())

print("\nWage data:")
print(wage_data.head())


# Save raw data
cpi_data.to_csv(
    "data/raw/cpi_raw.csv",
    index=False
)

wage_data.to_csv(
    "data/raw/wages_raw.csv",
    index=False
)


print("\nRaw data saved successfully.")