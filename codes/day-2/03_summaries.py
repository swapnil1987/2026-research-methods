"""Lecture 9: Grouped summaries and joins. Run from codes/day-2/."""
from pathlib import Path
Path("outputs").mkdir(exist_ok=True)

# Four households, two regions
import pandas as pd
small = pd.DataFrame({
    "id": ["A", "B", "C", "D"],
    "code": ["N", "N", "S", "S"],
    "income": [1000, 3000, 2000, 4000],
    "saving": [-100, 600, 400, 600],
})
print(small.to_string(index=False))

# One column, three summaries
print("Mean:", small["saving"].mean())
print("Median:", small["saving"].median())
print("Total:", small["saving"].sum())

# Several operations with agg
totals = small[["income", "saving"]].agg(
    ["mean", "median", "sum"]
)
print(totals.to_string())

# A mean within each region
regional = small.groupby(
    "code", as_index=False
)["saving"].mean()
print(regional.to_string(index=False))

# The calculation behind groupby
north = small.loc[small["code"] == "N", "saving"]
south = small.loc[small["code"] == "S", "saving"]
print("North:", north.tolist(), north.mean())
print("South:", south.tolist(), south.mean())

# Names for the output columns
regional = small.groupby("code", as_index=False).agg(
    households=("id", "size"),
    mean_saving=("saving", "mean"),
    total_saving=("saving", "sum"),
)
print(regional.to_string(index=False))

# The summary is another DataFrame
print(regional.columns.tolist())
print(regional["mean_saving"].tolist())
print(regional["households"].sum())

# Sort the regional comparison
ranked = regional.sort_values(
    "mean_saving", ascending=False
)
print(ranked[["code", "mean_saving"]].to_string(
    index=False
))

# Rows and observed values
observed = small.copy()
observed.loc[0, "saving"] = float("nan")
counts = observed.groupby("code", as_index=False).agg(
    rows=("id", "size"),
    saving_values=("saving", "count"),
)
print(counts.to_string(index=False))

# A comparison creates a Boolean column
small["shortfall"] = small["saving"] < 0
print(small[["id", "saving", "shortfall"]].to_string(
    index=False
))
print("Shortfalls:", small["shortfall"].sum())

# A Boolean mean is a proportion
rates = small.groupby("code", as_index=False).agg(
    households=("id", "size"),
    shortfall_rate=("shortfall", "mean"),
)
print(rates.to_string(index=False))

# Exercise 1: a regional comparison
small["saving_rate"] = (
    small["saving"] / small["income"]
)
# Group by code.
# Report households, median saving, and mean saving_rate.
# Sort the result by median saving, largest first.

# Exercise 1: worked answer
answer = small.groupby("code", as_index=False).agg(
    households=("id", "size"),
    median_saving=("saving", "median"),
    mean_rate=("saving_rate", "mean"),
)
answer = answer.sort_values("median_saving", ascending=False)
print(answer.round(3).to_string(index=False))

# A small denominator example
two = pd.DataFrame({
    "income": [1000, 3000],
    "saving": [200, 300],
})
two["rate"] = two["saving"] / two["income"]
print(two.to_string(index=False))

# Mean rate and pooled rate
mean_rate = two["rate"].mean()
pooled_rate = two["saving"].sum() / two["income"].sum()
print(f"Mean household rate: {mean_rate:.1%}")
print(f"Pooled saving rate:  {pooled_rate:.1%}")

# A separate table of region names
names = pd.DataFrame({
    "code": ["N", "S"],
    "region": ["North", "South"],
})
print(names.to_string(index=False))
print("Unique codes:", names["code"].is_unique)

# A left join keeps the household rows
joined = small.merge(
    names, on="code", how="left",
    validate="many_to_one",
)
print(joined[["id", "code", "region"]].to_string(
    index=False
))

# A duplicated lookup row multiplies data
bad_names = pd.concat(
    [names, names.iloc[[0]]], ignore_index=True
)
unchecked = small.merge(bad_names, on="code", how="left")
print("Households:", len(small))
print("Joined rows:", len(unchecked))

# Validation catches the duplicate key
try:
    small.merge(
        bad_names, on="code", how="left",
        validate="many_to_one",
    )
except pd.errors.MergeError as error:
    print(type(error).__name__)

# An unmatched code remains visible
unknown = small.copy()
unknown.loc[0, "code"] = "X"
joined = unknown.merge(names, on="code", how="left")
missing = joined.loc[joined["region"].isna(), ["id", "code"]]
print(missing.to_string(index=False))

# The full classroom sample
from lesson_data import load_households
df = load_households()
print("Households:", len(df))
print("Defined saving shares:", df["saving_share"].count())
print(df[["region", "saving"]].head(3).to_string(index=False))

# A summary of 195 households
summary = df.groupby("region", as_index=False).agg(
    households=("household_id", "size"),
    mean_saving=("saving", "mean"),
    median_saving=("saving", "median"),
)
print(summary.round(1).to_string(index=False))
assert summary["households"].sum() == len(df)

# Exercise 2: combine two summaries
df["shortfall"] = df["saving"] < 0
# Build one table: region, households, mean_saving.
# Build another: region, shortfall_rate.
# Join them on region, using validate="one_to_one".
# Sort by shortfall_rate, largest first.

# Exercise 2: worked answer
rates = df.groupby("region", as_index=False).agg(
    shortfall_rate=("shortfall", "mean"),
)
report = summary.merge(
    rates, on="region", how="left", validate="one_to_one"
).sort_values("shortfall_rate", ascending=False)
columns = ["region", "households", "mean_saving", "shortfall_rate"]
print(report[columns].round(3).to_string(index=False))
assert report["households"].sum() == len(df)
