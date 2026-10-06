# Data Dictionary

This table describes the variables used in the analysis, including their corresponding **FRED series**, definitions, units, and data frequency.

| Variable                    | FRED Series | Meaning                                                                           | Unit             | Frequency |
| --------------------------- | ----------- | --------------------------------------------------------------------------------- | ---------------- | --------- |
| **CPI**                     | `CPIAUCSL`  | Consumer price level                                                              | Index            | Monthly   |
| **Average Hourly Earnings** | `AHETPI`    | Average hourly earnings of production and nonsupervisory private-sector employees | Dollars per hour | Monthly   |
| **inflation_yoy**           | —           | Year-over-year change in consumer prices                                          | Percent          | Annual    |
| **wage_growth_yoy**         | —           | Year-over-year change in average hourly earnings                                  | Percent          | Annual    |


## Initial Data Quality Checks

- Both datasets contain monthly observations.
- Both datasets contain a date column and one measurement column.
- CPI is represented as a numerical index.
- Average hourly earnings are represented as numerical dollar values.
- The raw datasets contain historical observations going beyond our selected 2020-present analysis period.
- Duplicate-date and missing-value checks were performed using Python.
- Upon checking, there is 1 missing value in CPIAUCSL column

| Variable | Meaning | Calculation | Unit |
|---|---|---|---|
| inflation_yoy | Year-over-year change in consumer prices | CPI percentage change over 12 months | Percent |
| wage_growth_yoy | Year-over-year change in average hourly earnings | Wage percentage change over 12 months | Percent |