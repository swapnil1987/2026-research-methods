"""Lecture 7: Pandas basics. Run from codes/day-2/."""

# Six households in a DataFrame
import pandas as pd
df = pd.DataFrame({
    "id": ["A", "B", "C", "D", "E", "F"],
    "income": [1000, 1500, 800, 2000, 1200, 0],
    "consumption": [800, 1600, 700, 1400, 900, 200],
    "size": [1, 2, 1, 4, 2, 1],
    "region": ["N", "S", "N", "S", "N", "S"],
})
print(df.to_string(index=False))

# Rows, columns and a preview
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(2).to_string(index=False))

# A column or a table
income = df["income"]
one_column = df[["income"]]
print(type(income).__name__, income.shape)
print(type(one_column).__name__, one_column.shape)
print(income.head(3).to_string())

# Selecting columns in a different order
money = df[["id", "consumption", "income"]]
print(money.head(4).to_string(index=False))
print("Original columns:", len(df.columns))

# Arithmetic on whole columns
saving = df["income"] - df["consumption"]
print(saving.to_string(index=False))
print("Total saving:", saving.sum())

# Adding calculated columns
df["saving"] = df["income"] - df["consumption"]
df["income_pp"] = df["income"] / df["size"]
cols = ["id", "saving", "income_pp"]
print(df[cols].to_string(index=False))

# A comparison for every row
mask = df["saving"] < 0
print(mask.to_string(index=False))
print("Negative-saving households:", mask.sum())

# Filtering rows and selecting columns
mask = df["saving"] < 0
selected = df.loc[mask, ["id", "income", "saving"]]
print(selected.to_string(index=False))

# Selecting a list of categories
north = df["region"].isin(["N"])
both = df["region"].isin(["N", "S"])
print(df.loc[north, ["id", "region"]].to_string(index=False))
print("N or S:", both.sum())

# Two conditions in one filter
mask = (df["income"] <= 1200) & (df["size"] >= 2)
print(df.loc[mask, ["id", "income", "size"]].to_string(index=False))

# Worked answer · North and income
mask = (df["region"] == "N") & (df["income"] >= 1000)
selected = df.loc[mask, ["id", "income", "size"]]
print(selected.to_string(index=False))
print("Selected:", len(selected))

# Largest values first
ranked = df.sort_values("saving", ascending=False)
print(ranked[["id", "saving"]].head(3).to_string(index=False))
print("First ID in df:", df.iloc[0]["id"])

# Rows by position with iloc
first_two = ranked.iloc[:2]
print(first_two[["id", "saving"]].to_string())
print("One value:", ranked.iloc[0]["saving"])

# Row labels survive filtering
north = df.loc[df["region"] == "N", ["id", "income"]]
print(north.to_string())
print("Label 4:", north.loc[4, "income"])
print("Position 1:", north.iloc[1]["income"])

# Counting households by category
print(df["region"].value_counts().to_string())
print("All households:", len(df))
print("Sizes:", df["size"].value_counts().sort_index().to_dict())

# Quick numerical summaries
print("Mean income:", df["income"].mean())
print("Median income:", df["income"].median())
print("Saving range:", df["saving"].min(), df["saving"].max())
print("Total saving:", df["saving"].sum())

# Worked answer · A filter followed by a sort
mask = (df["income_pp"] >= 600) & (df["saving"] > 0)
selected = df.loc[mask, ["id", "income_pp", "saving"]]
selected = selected.sort_values("income_pp", ascending=False)
print(selected.to_string(index=False))
print("Selected saving:", selected["saving"].sum())

# Reading the classroom CSV
raw = pd.read_csv("data/raw/households.csv")
print("Shape:", raw.shape)
print(raw.head(3).to_string(index=False))

# A numeric-looking column can contain text
print(raw[["income", "consumption", "size"]].dtypes.to_string())
print(raw["income"].head(3).tolist())
print(raw.loc[raw["income"] == "missing", ["household_id", "income"]]
      .to_string(index=False))

# A selection from the larger file
mask = (raw["region_code"] == "N") & (raw["size"] == 2)
selected = raw.loc[mask, ["household_id", "size", "region_code"]]
print(selected.head(3).to_string(index=False))
print("Selected rows:", len(selected))
