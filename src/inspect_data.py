import pandas as pd


# Load raw datasets
cpi_data = pd.read_csv("data/raw/cpi_raw.csv")
wage_data = pd.read_csv("data/raw/wages_raw.csv")


def inspect_dataset(data, name):
    """Display basic information about a dataset."""

    print(f"\n{'=' * 50}")
    print(f"{name} DATASET")
    print(f"{'=' * 50}")

    print("\nFirst 5 rows:")
    print(data.head())

    print("\nShape:")
    print(data.shape)

    print("\nColumns:")
    print(data.columns.tolist())

    print("\nData types:")
    print(data.dtypes)

    print("\nMissing values:")
    print(data.isna().sum())

    print("\nDate range:")
    print(
        data["observation_date"].min(),
        "to",
        data["observation_date"].max()
    )

    print("\nDuplicate dates:")
    print(data["observation_date"].duplicated().sum())


# Inspect both datasets
inspect_dataset(cpi_data, "CPI")
inspect_dataset(wage_data, "WAGE")