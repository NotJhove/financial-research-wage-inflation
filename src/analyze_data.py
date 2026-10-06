import pandas as pd


# Load processed datasets
cpi_data = pd.read_csv(
    "data/processed/cpi_processed.csv"
)

wage_data = pd.read_csv(
    "data/processed/wages_processed.csv"
)


# Convert dates to datetime
cpi_data["observation_date"] = pd.to_datetime(
    cpi_data["observation_date"]
)

wage_data["observation_date"] = pd.to_datetime(
    wage_data["observation_date"]
)


# Merge CPI and wage data by date
analysis_data = pd.merge(
    cpi_data,
    wage_data,
    on="observation_date",
    how="inner"
)


# Calculate the wage growth minus inflation gap
analysis_data["wage_inflation_gap"] = (
    analysis_data["wage_growth_yoy"]
    - analysis_data["inflation_yoy"]
)


# Find the month with the highest inflation
inflation_peak = analysis_data.loc[
    analysis_data["inflation_yoy"].idxmax()
]


# Find the month with the highest wage growth
wage_growth_peak = analysis_data.loc[
    analysis_data["wage_growth_yoy"].idxmax()
]


# Find the largest negative wage-inflation gap
largest_negative_gap = analysis_data.loc[
    analysis_data["wage_inflation_gap"].idxmin()
]


# Count months when wage growth was ahead or behind inflation
wages_ahead = (
    analysis_data["wage_inflation_gap"] > 0
).sum()

wages_behind = (
    analysis_data["wage_inflation_gap"] < 0
).sum()


# Calculate average inflation and wage growth
average_inflation = analysis_data[
    "inflation_yoy"
].mean()

average_wage_growth = analysis_data[
    "wage_growth_yoy"
].mean()


# Calculate real hourly earnings
# January 2020 is used as the purchasing-power baseline.
base_cpi = analysis_data.loc[
    analysis_data["observation_date"] == "2020-01-01",
    "CPIAUCSL"
].iloc[0]

analysis_data["real_hourly_earnings"] = (
    analysis_data["AHETPI"]
    / analysis_data["CPIAUCSL"]
) * base_cpi


# Create a real earnings index
# January 2020 = 100
base_real_earnings = analysis_data.loc[
    analysis_data["observation_date"] == "2020-01-01",
    "real_hourly_earnings"
].iloc[0]

analysis_data["real_earnings_index"] = (
    analysis_data["real_hourly_earnings"]
    / base_real_earnings
) * 100


# Find the lowest real earnings after January 2020
post_2020_data = analysis_data[
    analysis_data["observation_date"] >= "2021-01-01"
]

real_earnings_low = post_2020_data.loc[
    post_2020_data["real_earnings_index"].idxmin()
]


# Find the highest real earnings in the analysis period
real_earnings_high = analysis_data.loc[
    analysis_data["real_earnings_index"].idxmax()
]


# Display key findings
print("\n===== KEY FINDINGS =====")

print(
    f"\nInflation peak: "
    f"{inflation_peak['observation_date'].strftime('%B %Y')}"
)

print(
    f"Inflation rate: "
    f"{inflation_peak['inflation_yoy']:.2f}%"
)

print(
    f"\nWage growth peak: "
    f"{wage_growth_peak['observation_date'].strftime('%B %Y')}"
)

print(
    f"Wage growth rate: "
    f"{wage_growth_peak['wage_growth_yoy']:.2f}%"
)

print(
    f"\nLargest negative wage-inflation gap: "
    f"{largest_negative_gap['wage_inflation_gap']:.2f} percentage points"
)

print(
    f"Occurred in: "
    f"{largest_negative_gap['observation_date'].strftime('%B %Y')}"
)

print(
    f"\nMonths wages grew faster than inflation: "
    f"{wages_ahead}"
)

print(
    f"Months wages grew slower than inflation: "
    f"{wages_behind}"
)

print(
    f"\nAverage inflation: "
    f"{average_inflation:.2f}%"
)

print(
    f"Average wage growth: "
    f"{average_wage_growth:.2f}%"
)

print(
    f"\nLowest post-2020 real earnings index: "
    f"{real_earnings_low['real_earnings_index']:.2f}"
)

print(
    f"Occurred in: "
    f"{real_earnings_low['observation_date'].strftime('%B %Y')}"
)

print(
    f"\nHighest real earnings index: "
    f"{real_earnings_high['real_earnings_index']:.2f}"
)

print(
    f"Occurred in: "
    f"{real_earnings_high['observation_date'].strftime('%B %Y')}"
)


# Save the final analysis dataset
analysis_data.to_csv(
    "data/processed/analysis_data.csv",
    index=False
)

print("\nAnalysis dataset saved successfully.")