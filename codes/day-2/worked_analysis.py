"""Worked Day 2 analysis. Run from codes/day-2/ in the course environment."""

# The observation and its units
income = 1000
consumption = 1100
saving = income - consumption
print(saving)

# Imports and the working folder
from pathlib import Path
import pandas as pd
import plotnine as pn
from IPython.display import HTML, display
from plotnine import (
    ggplot, aes, geom_point, geom_hline, geom_histogram,
    geom_boxplot, geom_col, facet_wrap, labs,
    theme_minimal, theme_gray, theme, element_blank, coord_flip,
)
print(Path.cwd().name)

# A CSV becomes a DataFrame
raw = pd.read_csv("data/raw/households.csv")
print(raw.shape)
print(raw.columns.tolist())

# Three observations
print(raw.head(3).to_string(index=False))

# Types and missing entries
print(raw.dtypes.to_string())
print(raw.isna().sum().to_string())

# Column selection
print(raw["size"].head(3).to_list())
money = raw[["income", "consumption"]]
print(money.shape)

# Row selection with loc
large = raw.loc[raw["size"] >= 4, ["household_id", "size"]]
print(large.head(3).to_string(index=False))
print(len(large))

# Exercise 1: a subset
# Select size == 2 and region_code == "N".
# Keep household_id, size, and region_code.
# Print three rows and the number of selected observations.

# Worked example: two conditions
selected = raw.loc[
    (raw["size"] == 2) & (raw["region_code"] == "N"),
    ["household_id", "size", "region_code"],
]
print(selected.head(3).to_string(index=False))
print(len(selected))

# An early plot from complete rows
preview = raw.copy()
preview["income"] = pd.to_numeric(preview["income"], errors="coerce")
preview = preview.dropna(subset=["income", "consumption"]).copy()
preview["saving"] = preview["income"] - preview["consumption"]
preview_plot = ggplot(preview, aes("income", "saving")) + geom_point()

# Preserving the raw input
clean = raw.copy()
print(raw.shape, clean.shape)

# Exact duplicates and household IDs
print(clean.duplicated().sum())
print(clean["household_id"].duplicated().sum())
clean = clean.drop_duplicates().copy()
assert clean["household_id"].is_unique
print(len(clean))

# Numeric conversion
clean["income"] = pd.to_numeric(clean["income"], errors="coerce")
print(clean[["income", "consumption"]].isna().sum().to_string())

# The exclusion record
incomplete = clean.loc[
    clean[["income", "consumption"]].isna().any(axis=1),
    ["household_id", "income", "consumption"],
]
print(incomplete.to_string(index=False))

# The complete-record policy
before = len(clean)
clean = clean.dropna(subset=["income", "consumption"]).copy()
print("Excluded:", before - len(clean), "Retained:", len(clean))
assert len(clean) == 195
assert (clean["size"] > 0).all()
assert (clean[["income", "consumption"]] >= 0).all().all()

# Vectorised calculations
clean["saving"] = clean["income"] - clean["consumption"]
clean["income_per_person"] = clean["income"] / clean["size"]
print(clean[["income", "consumption", "saving"]].head(3).to_string(index=False))

# Undefined shares
denominator = clean["income"].where(clean["income"] > 0)
clean["saving_share"] = clean["saving"] / denominator
print("Zero incomes:", (clean["income"] == 0).sum())
print("Defined shares:", clean["saving_share"].notna().sum())

# Exercise 2: zero-income households
# Select zero-income households.
# Print income, consumption, saving, and saving_share.
# Explain whether to exclude them from saving-amount totals.

# Worked example: amounts and shares
zero_income = clean.loc[
    clean["income"] == 0,
    ["income", "consumption", "saving", "saving_share"],
]
print(zero_income.to_string(index=False))
assert zero_income["saving_share"].isna().all()

# A region lookup
regions = pd.read_csv("data/raw/regions.csv")
print(regions.to_string(index=False))
assert regions["region_code"].is_unique

# A checked left join
n_before = len(clean)
df = clean.merge(
    regions, on="region_code", how="left",
    validate="many_to_one", indicator=True,
)
assert len(df) == n_before
assert df["_merge"].eq("both").all()
print(df["_merge"].value_counts().to_string())

# A duplicate key multiplies records
bad_lookup = pd.concat([regions, regions.iloc[[0]]], ignore_index=True)
unchecked = clean.merge(bad_lookup, on="region_code", how="left")
print("Before:", len(clean), "After:", len(unchecked))

# Grouped summaries
summary = df.groupby("region", as_index=False).agg(
    n_households=("household_id", "size"),
    mean_saving=("saving", "mean"),
    median_saving=("saving", "median"),
    n_shares=("saving_share", "count"),
    mean_share=("saving_share", "mean"),
)
print(summary.round(2).to_string(index=False))

# Mean household share and pooled share
mean_share = df["saving_share"].mean()
pooled_share = df["saving"].sum() / df["income"].sum()
print(f"Household mean: {mean_share:.2%}")
print(f"Pooled share: {pooled_share:.2%}")
print("Households:", len(df), "Defined shares:", df["saving_share"].count())

# Exercise 3: a regional shortfall rate
# Create negative_saving = saving < 0.
# For each region, calculate count and the fraction with negative saving.
# Include the zero-income households.

# Worked example: a Boolean group mean
df["negative_saving"] = df["saving"] < 0
shortfalls = df.groupby("region", as_index=False).agg(
    households=("household_id", "size"),
    shortfall_rate=("negative_saving", "mean"),
)
print(shortfalls.round(3).to_string(index=False))

# Data and position mappings
base = ggplot(df, aes(x="income", y="saving"))
points = base + geom_point()

# A constant colour
constant = base + geom_point(color="#245b78", alpha=0.6)

# Colour mapped to region
coloured = (
    ggplot(df, aes("income", "saving", color="region"))
    + geom_point(alpha=0.6)
    + labs(color="Region")
)

# Facets and shared scales
faceted = (
    base + geom_point(color="#245b78", alpha=0.6)
    + facet_wrap("region", ncol=2)
    + theme_minimal(base_size=16)
)

# A distribution plot
histogram = (
    ggplot(df, aes("saving"))
    + geom_histogram(binwidth=250, boundary=0, fill="#245b78")
    + labs(x="Monthly saving (EUR)", y="Households")
    + theme_minimal(base_size=16)
)

# A supplied summary height
regional_bars = (
    ggplot(summary, aes("region", "mean_saving"))
    + geom_col(fill="#245b78")
    + labs(x="Region", y="Mean monthly saving (EUR)")
    + theme_minimal(base_size=16)
)

# Within-region variation
boxes = (
    ggplot(df, aes("region", "saving"))
    + geom_boxplot(fill="#b9d3df", outlier_alpha=0.4)
    + labs(x="Region", y="Monthly saving (EUR)")
    + theme_minimal(base_size=16)
)

# Exercise 4: faceted histograms
# Plot saving with 250 EUR bins.
# Make one panel per region with common axes.
# Label the money axis and household counts.

# Worked example: conditional distributions
regional_hist = (
    ggplot(df, aes("saving"))
    + geom_histogram(binwidth=250, boundary=0, fill="#245b78")
    + facet_wrap("region", ncol=2)
    + labs(x="Monthly saving (EUR)", y="Households")
    + theme_minimal(base_size=16)
)

# A weak presentation
bad = (
    base + geom_point(color="#ef5350", size=5)
    + labs(title="Results", x="x", y="y")
    + theme_gray(base_size=12)
)

# Labels, reference line, and source
good = (
    base + geom_hline(yintercept=0, color="#777777", size=0.5)
    + geom_point(color="#245b78", alpha=0.6, size=1.8)
    + labs(title="Household saving and income",
           x="Monthly income (EUR)", y="Monthly saving (EUR)",
           caption=f"Synthetic classroom data; n = {len(df)} households")
    + theme_minimal(base_size=16)
)

# Scale decisions
print("Minimum saving:", df["saving"].min())
print("Negative-saving households:", (df["saving"] < 0).sum())

# An explicit category order
region_order = summary.sort_values("mean_saving")["region"].tolist()
ordered_summary = summary.copy()
ordered_summary["region"] = pd.Categorical(
    ordered_summary["region"], categories=region_order, ordered=True
)

# An ordered horizontal chart
ordered_plot = (
    ggplot(ordered_summary, aes("region", "mean_saving"))
    + geom_col(fill="#245b78") + coord_flip()
    + labs(x="Region", y="Mean monthly saving (EUR)")
    + theme_minimal(base_size=16)
)

# Exercise 5: design for projection
# Start from good and facet by region.
# Keep common scales and increase text size.
# Remove minor gridlines.

# Worked example: a presentation figure
slide_plot = (
    good + facet_wrap("region", ncol=2)
    + theme(text=pn.element_text(size=18),
            panel_grid_minor=element_blank())
)

# The numerical summary
table = summary.copy()
print(table.round(2).to_string(index=False))

# Readable percentage labels
display_table = table.copy()
display_table["Mean share (%)"] = 100 * display_table["mean_share"]
display_table = display_table.rename(columns={
    "region": "Region", "n_households": "Households",
    "n_shares": "Defined shares", "mean_saving": "Mean saving (EUR)",
})

# A compact display table
columns = ["Region", "Households", "Defined shares",
           "Mean saving (EUR)", "Mean share (%)"]
html_table = display_table[columns].to_html(
    index=False, float_format=lambda value: f"{value:.1f}"
)
display(HTML(html_table))

# Exercise 6: median income per person
# Calculate median income per person by region.
# Join this four-row result to table using region.
# Verify four rows and no unmatched regions.

# Worked example: combining summaries
medians = df.groupby("region", as_index=False).agg(
    median_income_per_person=("income_per_person", "median")
)
extended = table.merge(
    medians, on="region", how="left", validate="one_to_one"
)
assert len(extended) == 4
assert extended["median_income_per_person"].notna().all()
median_columns = ["region", "median_income_per_person"]
print(extended[median_columns].round(1).to_string(index=False))

# Export dimensions and formats
output = Path("outputs")
output.mkdir(exist_ok=True)
good.save(output / "saving_income.png", width=8, height=4.5,
          dpi=200, verbose=False)
good.save(output / "saving_income.pdf", width=8, height=4.5,
          verbose=False)

# Unrounded numerical exports
summary.to_csv(output / "regional_summary.csv", index=False)
clean.to_csv(output / "checked_households.csv", index=False)
(output / "regional_table.html").write_text(html_table)
print((output / "regional_summary.csv").is_file())

# Worked workflow: preparing the sample
fresh = pd.read_csv("data/raw/households.csv").drop_duplicates()
fresh["income"] = pd.to_numeric(fresh["income"], errors="coerce")
fresh = fresh.dropna(subset=["income", "consumption"]).copy()
assert fresh["household_id"].is_unique
assert (fresh["size"] > 0).all()
fresh["saving"] = fresh["income"] - fresh["consumption"]
positive_income = fresh["income"].where(fresh["income"] > 0)
fresh["saving_share"] = fresh["saving"] / positive_income

# Worked workflow: the region join
lookup = pd.read_csv("data/raw/regions.csv")
fresh = fresh.merge(
    lookup, on="region_code", how="left",
    validate="many_to_one", indicator=True,
)
assert len(fresh) == 195
assert fresh["_merge"].eq("both").all()
assert fresh["saving_share"].count() == 193

# Worked workflow: a final table
final_summary = fresh.groupby("region", as_index=False).agg(
    households=("household_id", "size"),
    mean_saving=("saving", "mean"),
    defined_shares=("saving_share", "count"),
)
assert final_summary["households"].sum() == len(fresh)
final_summary.to_csv(output / "lab_summary.csv", index=False)

preview_plot.save(output / "preview_plot.png",width=9,height=4.6,dpi=150,verbose=False)

points.save(output / "points.png",width=9,height=4.6,dpi=150,verbose=False)

coloured.save(output / "coloured.png",width=9,height=4.6,dpi=150,verbose=False)

faceted.save(output / "faceted.png",width=9,height=4.6,dpi=150,verbose=False)

histogram.save(output / "histogram.png",width=9,height=4.6,dpi=150,verbose=False)

regional_bars.save(output / "regional_bars.png",width=9,height=4.6,dpi=150,verbose=False)

boxes.save(output / "boxes.png",width=9,height=4.6,dpi=150,verbose=False)

regional_hist.save(output / "regional_hist.png",width=9,height=4.6,dpi=150,verbose=False)

bad.save(output / "bad.png",width=9,height=4.6,dpi=150,verbose=False)

good.save(output / "good.png",width=9,height=4.6,dpi=150,verbose=False)

ordered_plot.save(output / "ordered_plot.png",width=9,height=4.6,dpi=150,verbose=False)

slide_plot.save(output / "slide_plot.png",width=9,height=4.6,dpi=150,verbose=False)

print("Completed: 195 checked households, 193 defined saving shares.")
