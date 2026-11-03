"""A first checked analysis of four synthetic households.

Run from codes/lecture-6/: python first_dataset.py
Input amounts are EUR per month, survey year 2026. No real people are represented.
"""

from pathlib import Path

import pandas as pd


data_path = Path("data/raw/households.csv")
households = pd.read_csv(data_path)
assert households.shape == (4, 6)
assert households["household_id"].is_unique
assert households["income_eur_month"].notna().all()
assert households["consumption_eur_month"].notna().all()
assert (households["household_size"] > 0).all()

analysis = households.copy()
analysis["saving_eur_month"] = (
    analysis["income_eur_month"] - analysis["consumption_eur_month"]
)
analysis["income_per_person"] = (
    analysis["income_eur_month"] / analysis["household_size"]
)

# Hand-check the fourth household and the total across all four.
assert analysis.iloc[3]["saving_eur_month"] == -50
assert analysis["saving_eur_month"].sum() == 1050

negative_saving = analysis["saving_eur_month"] < 0
print("Rows and columns:", households.shape)
print("Saving by household:", analysis["saving_eur_month"].to_list())
print("Negative-saving household IDs:", analysis.loc[negative_saving, "household_id"].to_list())
print(f"Total saving: {analysis['saving_eur_month'].sum():.2f} EUR/month")
print(f"Mean saving: {analysis['saving_eur_month'].mean():.2f} EUR/household/month")

output_path = Path("outputs/household_saving.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
analysis[["household_id", "saving_eur_month"]].to_csv(output_path, index=False)

reloaded = pd.read_csv(output_path)
assert reloaded.shape == (4, 2)
assert reloaded["saving_eur_month"].to_list() == [200, 400, 500, -50]
print("Saved and checked:", output_path)
