"""Lecture 8: Preparing data. Run from codes/day-2/."""

# The input before any changes
import pandas as pd
raw = pd.read_csv("data/raw/households.csv")
clean = raw.copy()
print("Source rows:", len(raw))
print(clean.head(3).to_string(index=False))

# An exact duplicate
tiny = pd.DataFrame({
    "id": ["A", "A", "B"],
    "income": [1000, 1000, 1500],
})
print("Duplicate rows:", tiny.duplicated().tolist())
print(tiny.drop_duplicates().to_string(index=False))

# The same ID can hide conflicting values
conflict = pd.DataFrame({
    "id": ["A", "A", "B"],
    "income": [1000, 1200, 1500],
})
print("Exact duplicates:", conflict.duplicated().sum())
print(conflict.loc[conflict["id"].duplicated(keep=False)]
      .to_string(index=False))

# Removing the repeated classroom record
print("Exact duplicates:", clean.duplicated().sum())
clean = clean.drop_duplicates().copy()
print("Rows after deduplication:", len(clean))
print("Unique IDs:", clean["household_id"].is_unique)

# Converting text to numbers
text_income = pd.Series(["1000", "missing", "", None])
numeric = pd.to_numeric(text_income, errors="coerce")
print(pd.DataFrame({
    "input": text_income, "numeric": numeric,
}).to_string(index=False))

# Converting the income column
print("Before:", clean["income"].dtype)
clean["income"] = pd.to_numeric(clean["income"], errors="coerce")
print("After:", clean["income"].dtype)
print(clean[["income", "consumption"]].isna().sum().to_string())

# Zero income is an observed value
income = pd.Series([1000.0, 0.0, None])
print("Income:", income.tolist())
print("Missing:", income.isna().tolist())
print("Zero:", income.eq(0).tolist())

# Finding the incomplete records
required = ["income", "consumption"]
incomplete = clean[required].isna().any(axis=1)
cols = ["household_id", "income", "consumption"]
print(clean.loc[incomplete, cols].to_string(index=False))

# Worked answer · Five exclusions, two zeros retained
before = len(clean)
clean = clean.dropna(subset=required).copy()
print("Before:", before, "After:", len(clean))
print("Zero incomes:", clean["income"].eq(0).sum())
print("Original rows:", len(raw))

# Saving for every retained household
clean["saving"] = clean["income"] - clean["consumption"]
cols = ["household_id", "income", "consumption", "saving"]
print(clean[cols].head(4).to_string(index=False))
print("Negative saving:", clean["saving"].lt(0).sum())

# Income per person
clean["income_per_person"] = clean["income"] / clean["size"]
cols = ["household_id", "income", "size", "income_per_person"]
print(clean[cols].head(3).round(2).to_string(index=False))
print("Nonpositive sizes:", clean["size"].le(0).sum())

# Division by zero in a column
example = pd.DataFrame({
    "income": [1000.0, 0.0],
    "consumption": [800.0, 200.0],
})
example["saving"] = example["income"] - example["consumption"]
example["share"] = example["saving"] / example["income"]
print(example.to_string(index=False))

# A denominator only where income is positive
income = pd.Series([1000.0, 0.0, 800.0])
denominator = income.where(income > 0)
print(pd.DataFrame({
    "income": income, "denominator": denominator,
}).to_string(index=False))

# Amounts remain defined when shares are missing
denominator = clean["income"].where(clean["income"] > 0)
clean["saving_share"] = clean["saving"] / denominator
cols = ["household_id", "income", "saving", "saving_share"]
print(clean.loc[clean["income"].eq(0), cols].to_string(index=False))
print("Defined shares:", clean["saving_share"].count())

# Worked answer · Three conditions
clean["negative_saving"] = clean["saving"] < 0
mask = (
    (clean["size"] >= 3) & (clean["income_per_person"] < 750)
    & clean["negative_saving"]
)
cols = ["household_id", "size", "income_per_person", "saving"]
selected = clean.loc[mask, cols]
print(selected.head(3).round(2).to_string(index=False))
print("Selected:", len(selected))

# Checks that match the data definitions
assert clean["household_id"].is_unique
assert clean["size"].gt(0).all()
assert clean[["income", "consumption"]].ge(0).all().all()
assert clean[required].notna().all().all()
print("Passed: IDs, sizes, money inputs and required values")

# Selecting suspicious rows for inspection
check = pd.DataFrame({
    "id": ["A", "B", "C"], "income": [1000, -100, 800],
    "size": [2, 1, 0],
})
bad = (check["income"] < 0) | (check["size"] <= 0)
print(check.loc[bad].to_string(index=False))

# Rounding a display keeps the underlying values
values = pd.Series([1000 / 3, 800 / 3])
print("Display:", values.round(1).tolist())
print("Stored:", values.tolist())
print("Mean from stored values:", values.mean())

# A preparation function
def prepare_households(source):
    out = source.drop_duplicates().copy()
    out["income"] = pd.to_numeric(out["income"], errors="coerce")
    out = out.dropna(subset=["income", "consumption"]).copy()
    out["saving"] = out["income"] - out["consumption"]
    out["income_per_person"] = out["income"] / out["size"]
    denominator = out["income"].where(out["income"] > 0)
    out["saving_share"] = out["saving"] / denominator
    return out

prepared = prepare_households(raw)
print("Prepared households:", len(prepared))

# Checking a fresh preparation run
fresh = prepare_households(pd.read_csv("data/raw/households.csv"))
assert len(fresh) == 195
assert fresh["household_id"].is_unique
assert fresh["saving_share"].count() == 193
print(fresh[["saving", "income_per_person"]].head(3).to_string(index=False))

# Exporting the prepared table
from pathlib import Path
Path("outputs").mkdir(exist_ok=True)
fresh.to_csv("outputs/prepared_households.csv", index=False)
check = pd.read_csv("outputs/prepared_households.csv")
print("Exported rows:", len(check))
print("Undefined shares:", check["saving_share"].isna().sum())
