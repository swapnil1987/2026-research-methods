"""Figure design. Run from codes/day-2 in the course environment."""

# The same 195 households
from pathlib import Path
import pandas as pd
import plotnine as pn
from lesson_data import load_households
df = load_households()
print("Households:", len(df))
print("Negative saving:", (df["saving"] < 0).sum())

# The default scatterplot
base = pn.ggplot(df,
    pn.aes("income", "saving"))
default = base + pn.geom_point()
default

# Axis labels and a useful title
labelled = base + pn.labs(
    title="Household saving and income",
    x="Monthly income (EUR)",
    y="Monthly saving (EUR)",
)
p = labelled + pn.geom_point()
p

# Point size and transparency
points = labelled + pn.geom_point(
    color="#286482",
    alpha=0.55,
    size=1.8,
)
points

# The zero-saving reference
zero = points + pn.geom_hline(
    yintercept=0,
    color="#777777",
    size=0.5,
)
zero

# A quieter background
clean = (
    zero
    + pn.theme_minimal(base_size=15)
    + pn.theme(
        panel_grid_minor=(
            pn.element_blank())
    )
)
clean

# The caption identifies the sample
finished = clean + pn.labs(
    caption=(
        "Synthetic classroom data"
        f" | n = {len(df)} households"
    )
)
finished

# Exercise 1 · Consumption and income
# Use the same df.
# Put income on x and consumption on y.
# Add a 45-degree reference line.
# Use labels, alpha, a theme, and a caption.

# Worked answer · Consumption and income
spending = (
    pn.ggplot(df,
        pn.aes("income", "consumption"))
    + pn.geom_abline(slope=1, intercept=0)
    + pn.geom_point(alpha=0.5,
        color="#286482")
    + pn.labs(x="Monthly income (EUR)",
        y="Monthly consumption (EUR)",
        caption=("Synthetic households"
            " | n=195"))
    + pn.theme_minimal(base_size=15)
)
spending

# Colour identifies a variable
by_region = (
    pn.ggplot(df,
        pn.aes("income", "saving",
               color="region"))
    + pn.geom_point(alpha=0.65)
    + pn.labs(x="Income (EUR)",
        y="Saving (EUR)", color="Region")
    + pn.theme_minimal(base_size=15)
)
by_region

# An explicit four-colour palette
palette = {
    "East": "#0072B2",
    "North": "#D55E00",
    "South": "#009E73",
    "West": "#CC79A7",
}
coloured = (
    by_region
    + pn.scale_color_manual(
        values=palette)
)
coloured

# Common axes across panels
panels = (
    coloured
    + pn.facet_wrap("region", ncol=2)
    + pn.theme(legend_position="none")
)
panels

# The numbers behind a comparison
summary = df.groupby("region", as_index=False).agg(
    households=("household_id", "size"),
    mean_saving=("saving", "mean"),
)
print(summary.round(1).to_string(index=False))

# Alphabetical category order
bars = (
    pn.ggplot(summary,
        pn.aes("region", "mean_saving"))
    + pn.geom_col(fill="#286482")
    + pn.labs(x="Region",
        y="Mean monthly saving (EUR)")
    + pn.theme_minimal(base_size=15)
)
bars

# Ordering is part of the data
order = summary.sort_values(
    "mean_saving"
)["region"].tolist()
ordered = summary.copy()
ordered["region"] = pd.Categorical(
    ordered["region"], categories=order,
    ordered=True,
)
ordered["value"] = ordered["mean_saving"].round(1)
print(order)

# Horizontal bars and direct labels
ranked = (
    pn.ggplot(ordered,
        pn.aes("region", "mean_saving"))
    + pn.geom_col(fill="#286482")
    + pn.geom_text(pn.aes(label="value"),
        ha="left", nudge_y=8, size=11)
    + pn.expand_limits(y=430)
    + pn.coord_flip()
    + pn.labs(x="",
        y="Mean saving (EUR/month)")
    + pn.theme_minimal(base_size=15)
)
ranked

# A zoom excludes some values from view
inside = df["saving"].between(0, 1000)
print("All households:", len(df))
print("Within 0 to 1000:", inside.sum())
print("Median, all:", df["saving"].median())
print("Median, selected:", df.loc[
    inside, "saving"].median())

# Scale limits change boxplot statistics
box = (
    pn.ggplot(df,
        pn.aes("region", "saving"))
    + pn.geom_boxplot(fill="#A9CBDC")
    + pn.theme_minimal(base_size=15)
)
limited = box + pn.scale_y_continuous(
    limits=(0, 1000)
)
limited

# Coordinate limits zoom the full boxplot
zoomed = box + pn.coord_cartesian(
    ylim=(0, 1000)
)
zoomed

# Exercise 2 · Rank median income
# Calculate median income per person by region.
# Order the categories by that median.
# Make a horizontal bar or point chart.
# Label the units and display each value.

# Worked answer · The median table
medians = df.groupby("region", as_index=False).agg(
    median_income=("income_per_person", "median")
)
order = medians.sort_values(
    "median_income")["region"].tolist()
medians["region"] = pd.Categorical(
    medians["region"], categories=order,
    ordered=True,
)
medians["value"] = medians["median_income"].round(1)
print(medians.round(1).to_string(index=False))

# Worked answer · The ranked plot
median_plot = (
    pn.ggplot(medians,
        pn.aes("region", "median_income"))
    + pn.geom_col(fill="#0072B2")
    + pn.geom_text(pn.aes(label="value"),
        ha="left", nudge_y=15, size=11)
    + pn.expand_limits(y=1200)
    + pn.coord_flip()
    + pn.labs(x="", y=("Median income"
        " (EUR/person/month)"))
    + pn.theme_minimal(base_size=15)
)
median_plot

# PNG for slides, PDF for print
output = Path("outputs")
output.mkdir(exist_ok=True)
median_plot.save(
    output / "median-income.png",
    width=9, height=5, dpi=200, verbose=False,
)
median_plot.save(
    output / "median-income.pdf",
    width=9, height=5, verbose=False,
)
print((output / "median-income.png").is_file())
