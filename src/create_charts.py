import pandas as pd
import matplotlib.pyplot as plt


# Load analysis dataset
analysis_data = pd.read_csv(
    "data/processed/analysis_data.csv"
)

analysis_data["observation_date"] = pd.to_datetime(
    analysis_data["observation_date"]
)

# Chart 1: Inflation

plt.figure(figsize=(12, 6))

plt.plot(
    analysis_data["observation_date"],
    analysis_data["inflation_yoy"],
    linewidth=2,
    label="Inflation"
)

plt.axhline(
    y=2,
    linestyle="--",
    linewidth=1,
    label="2% benchmark"
)


# Identify inflation peak
inflation_peak = analysis_data.loc[
    analysis_data["inflation_yoy"].idxmax()
]

plt.scatter(
    inflation_peak["observation_date"],
    inflation_peak["inflation_yoy"],
    s=60,
    zorder=5
)

plt.annotate(
    f'{inflation_peak["inflation_yoy"]:.1f}% peak\n'
    f'{inflation_peak["observation_date"].strftime("%b %Y")}',
    xy=(
        inflation_peak["observation_date"],
        inflation_peak["inflation_yoy"]
    ),
    xytext=(20, -20),
    textcoords="offset points",
    fontsize=10
)

plt.title(
    "U.S. Inflation Surged to Nearly 9% in 2022",
    fontsize=16
)

plt.xlabel("Date")
plt.ylabel("Year-over-Year Inflation (%)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    "charts/chart_1_inflation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Chart 2: Inflation vs. Wage Growth

plt.figure(figsize=(12, 6))

plt.plot(
    analysis_data["observation_date"],
    analysis_data["inflation_yoy"],
    linewidth=2,
    label="Inflation"
)

plt.plot(
    analysis_data["observation_date"],
    analysis_data["wage_growth_yoy"],
    linewidth=2,
    label="Wage Growth"
)


# Identify inflation peak and corresponding wage growth
inflation_peak = analysis_data.loc[
    analysis_data["inflation_yoy"].idxmax()
]

gap = (
    inflation_peak["wage_growth_yoy"]
    - inflation_peak["inflation_yoy"]
)


plt.scatter(
    inflation_peak["observation_date"],
    inflation_peak["inflation_yoy"],
    s=60,
    zorder=5
)

plt.scatter(
    inflation_peak["observation_date"],
    inflation_peak["wage_growth_yoy"],
    s=60,
    zorder=5
)


# Inflation label
plt.annotate(
    f'{inflation_peak["inflation_yoy"]:.2f}%',
    xy=(
        inflation_peak["observation_date"],
        inflation_peak["inflation_yoy"]
    ),
    xytext=(20, -20),
    textcoords="offset points",
    fontsize=10
)


# Wage growth label
plt.annotate(
    f'{inflation_peak["wage_growth_yoy"]:.2f}%',
    xy=(
        inflation_peak["observation_date"],
        inflation_peak["wage_growth_yoy"]
    ),
    xytext=(15, -5),
    textcoords="offset points",
    fontsize=10
)


# Gap label
plt.annotate(
    f"Gap: {gap:.2f} pp",
    xy=(
        inflation_peak["observation_date"],
        inflation_peak["wage_growth_yoy"]
    ),
    xytext=(-35, 30),
    textcoords="offset points",
    fontsize=10
)

plt.title(
    "Inflation Outpaced Wage Growth During the 2022 Surge",
    fontsize=16
)

plt.xlabel("Date")
plt.ylabel("Year-over-Year Growth (%)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    "charts/chart_2_inflation_vs_wages.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# Chart 3: Real Purchasing Power
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    analysis_data["observation_date"],
    analysis_data["real_earnings_index"],
    linewidth=2,
    label="Real hourly earnings"
)

plt.axhline(
    y=100,
    linestyle="--",
    linewidth=1,
    label="January 2020 baseline"
)


# Find the lowest real earnings index after 2020
post_inflation_data = analysis_data[
    analysis_data["observation_date"] >= "2021-01-01"
]

real_earnings_low = post_inflation_data.loc[
    post_inflation_data["real_earnings_index"].idxmin()
]


plt.scatter(
    real_earnings_low["observation_date"],
    real_earnings_low["real_earnings_index"],
    s=60,
    zorder=5
)

plt.annotate(
    f'{real_earnings_low["real_earnings_index"]:.2f}\n'
    f'{real_earnings_low["observation_date"].strftime("%b %Y")}',
    xy=(
        real_earnings_low["observation_date"],
        real_earnings_low["real_earnings_index"]
    ),
    xytext=(15, -35),
    textcoords="offset points",
    fontsize=10
)

plt.title(
    "Real Hourly Earnings Dipped During the Inflation Surge, Then Recovered",
    fontsize=16
)

plt.xlabel("Date")
plt.ylabel("Real Earnings Index (Jan. 2020 = 100)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    "charts/chart_3_real_earnings.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("All charts generated successfully.")