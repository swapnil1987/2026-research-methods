"""Tables and a research report. Run from codes/day-2 in the course environment."""

# The data behind the table
from pathlib import Path
import math
import pandas as pd
import plotnine as pn
from IPython.display import HTML, display
from lesson_data import load_households
df = load_households()
output = Path("outputs")
output.mkdir(exist_ok=True)
print(len(df), df["saving_share"].count())

# One variable, several statistics
saving = pd.Series([0, 100, 200, 300, 1400])
print(saving.agg(["count", "mean", "median"]))

# The regional table
summary = df.groupby("region", as_index=False).agg(
    households=("household_id", "size"),
    mean_saving=("saving", "mean"),
    median_saving=("saving", "median"),
)
print(summary.round(1).to_string(index=False))

# The denominator next to the statistic
shares = df.groupby("region", as_index=False).agg(
    households=("household_id", "size"),
    defined_shares=("saving_share", "count"),
    mean_share=("saving_share", "mean"),
)
print(shares.round(3).to_string(index=False))

# Rounding a displayed copy
precision = summary[["region", "mean_saving"]].copy()
precision["display"] = precision["mean_saving"].round(1)
print(precision.to_string(index=False))

# Fractions and percent labels
share = 0.1234
print(f"{share:.3f}")
print(f"{share:.1%}")
print(f"{100 * share:.1f}%")

# A table with readable headings
view = summary.rename(columns={
    "region": "Region",
    "households": "Households",
    "mean_saving": "Mean saving (EUR)",
    "median_saving": "Median saving (EUR)",
})
print(view.round(1).to_string(index=False))

# A deliberate column order
columns = ["Region", "Households",
           "Median saving (EUR)", "Mean saving (EUR)"]
view = view[columns]
print(view.columns.tolist())

# The notebook's HTML table
html_table = view.to_html(
    index=False,
    float_format=lambda number: f"{number:.1f}",
)
display(HTML(html_table))

# Exercise 1 · An income table
# One row per region.
# Include households and median income_per_person.
# Sort the largest median first.
# Give the money column a readable heading.

# Worked answer · Median income per person
income_table = df.groupby(
    "region", as_index=False
).agg(
    households=("household_id", "size"),
    median_income=("income_per_person", "median"),
).sort_values("median_income", ascending=False)
income_view = income_table.rename(columns={
    "median_income": "Median EUR/person/month"
})
print(income_view.round(1).to_string(index=False))

# The CSV keeps numerical precision
path = output / "saving-summary.csv"
summary.to_csv(path, index=False)
reloaded = pd.read_csv(path)
assert math.isclose(
    reloaded.loc[0, "mean_saving"],
    summary.loc[0, "mean_saving"],
)
print(reloaded.shape)
print(path.is_file())

# The HTML table can travel with the report
table_path = output / "saving-summary.html"
table_path.write_text(
    html_table, encoding="utf-8"
)
print(table_path.is_file())
print("Rows:", len(view))

# A reusable summary function
def report_table(data):
    return data.groupby("region", as_index=False).agg(
        households=("household_id", "size"),
        median_income=("income_per_person", "median"),
        mean_saving=("saving", "mean"),
    ).sort_values("median_income", ascending=False)

# The same function on a fresh sample
fresh = load_households()
report = report_table(fresh)
print(report.round(1).to_string(index=False))
print("Households:", report["households"].sum())
assert report["households"].sum() == len(fresh)

# The table supplies the plot's heights
report_plot = (
    pn.ggplot(report,
        pn.aes("region", "median_income"))
    + pn.geom_col(fill="#286482")
    + pn.labs(x="Region",
        y=("Median income"
           " (EUR/person/month)"))
    + pn.theme_minimal(base_size=15)
)
report_plot

# Exercise 2 · A report for larger households
# Keep households with size >= 3.
# Reuse report_table on that sample.
# Plot regional median income per person.
# Export the numerical table and a PNG.

# Worked answer · The sample and table
large = fresh.loc[fresh["size"] >= 3].copy()
large_report = report_table(large)
print("Retained:", len(large))
print(large_report.round(1).to_string(index=False))
assert large_report["households"].sum() == len(large)
large_report.to_csv(
    output / "large-households.csv", index=False
)

# Worked answer · The labelled figure
large_plot = (
    pn.ggplot(large_report,
        pn.aes("region", "median_income"))
    + pn.geom_col(fill="#0072B2")
    + pn.labs(x="Region",
        y=("Median income"
           " (EUR/person/month)"),
        caption=("Size >=3"
            f" | n={len(large)}"))
    + pn.theme_minimal(base_size=15)
)
large_plot

# A complete run produces the report files
large_plot.save(
    output / "large-households.png",
    width=9, height=5, dpi=200, verbose=False,
)
expected = [
    "saving-summary.csv", "saving-summary.html",
    "large-households.csv", "large-households.png",
]
assert all((output / name).is_file() for name in expected)
print("\n".join(expected))
