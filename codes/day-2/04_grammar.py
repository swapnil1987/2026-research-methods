"""Lecture 10: Grammar of graphics with plotnine. Run from codes/day-2/."""
from pathlib import Path
Path("outputs").mkdir(exist_ok=True)

# The data for the first figure
import plotnine as pn
pn.theme_set(pn.theme_gray(base_size=16))
from lesson_data import load_households
df = load_households()
columns = ["income", "saving", "region"]
print(df[columns].head(3).to_string(index=False))
print("Households:", len(df))

# Data, mapping, and a point layer
p = (
    pn.ggplot(
        df,
        pn.aes("income", "saving")
    )
    + pn.geom_point()
)
p

p.save("outputs/10-02.png", width=7.4, height=4.9, dpi=145, verbose=False)

# Changing the mapping swaps the axes
p = (
    pn.ggplot(
        df, pn.aes(
            x="saving", y="income"
        )
    )
    + pn.geom_point()
)
p

p.save("outputs/10-03.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A constant colour belongs outside aes
base = pn.ggplot(
    df, pn.aes("income", "saving")
)
p = base + pn.geom_point(
    color="#245b78", alpha=0.55
)
p

p.save("outputs/10-04.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A variable colour belongs inside aes
p = (
    pn.ggplot(
        df, pn.aes(
            "income", "saving",
            color="region"
        )
    )
    + pn.geom_point(alpha=0.6)
)
p

p.save("outputs/10-05.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A numeric colour uses a gradient
p = (
    pn.ggplot(
        df, pn.aes(
            "income", "saving",
            color="size"
        )
    )
    + pn.geom_point(alpha=0.7)
)
p

p.save("outputs/10-06.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A second layer marks zero saving
p = (
    base
    + pn.geom_hline(
        yintercept=0, color="#777777"
    )
    + pn.geom_point(alpha=0.55)
)
p

p.save("outputs/10-07.png", width=7.4, height=4.9, dpi=145, verbose=False)

# Exercise 1: two-person households
pairs = df.loc[df["size"] == 2].copy()
print("Households to plot:", len(pairs))
# Use pairs as the data.
# Map income to x and saving to y.
# Map region to colour.
# Add points with alpha=0.6 and a line at y=0.

# Exercise 1: worked answer
p = (
    pn.ggplot(
        pairs, pn.aes(
            "income", "saving",
            color="region"
        )
    )
    + pn.geom_hline(yintercept=0)
    + pn.geom_point(alpha=0.6)
)
p

p.save("outputs/10-09.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A histogram counts observations in bins
p = (
    pn.ggplot(df, pn.aes("saving"))
    + pn.geom_histogram(
        binwidth=250,
        fill="#245b78", color="white"
    )
)
p

p.save("outputs/10-10.png", width=7.4, height=4.9, dpi=145, verbose=False)

# Bin width changes the visible pattern
p = (
    pn.ggplot(df, pn.aes("saving"))
    + pn.geom_histogram(
        binwidth=1000,
        fill="#245b78", color="white"
    )
)
p

p.save("outputs/10-11.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A bar chart can count raw rows
p = (
    pn.ggplot(df, pn.aes("region"))
    + pn.geom_bar(fill="#245b78")
)
p

p.save("outputs/10-12.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A table can already contain the heights
summary = df.groupby("region", as_index=False).agg(
    households=("household_id", "size"),
    mean_saving=("saving", "mean"),
)
print(summary.round(1).to_string(index=False))

# geom_bar still counts summary rows
p = (
    pn.ggplot(
        summary, pn.aes("region")
    )
    + pn.geom_bar(fill="#245b78")
)
p

p.save("outputs/10-14.png", width=7.4, height=4.9, dpi=145, verbose=False)

# geom_col uses supplied heights
p = (
    pn.ggplot(
        summary, pn.aes(
            "region", "mean_saving"
        )
    )
    + pn.geom_col(fill="#245b78")
)
p

p.save("outputs/10-15.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A boxplot compares distributions
p = (
    pn.ggplot(
        df,
        pn.aes("region", "saving")
    )
    + pn.geom_boxplot(fill="#dbe7ed")
)
p

p.save("outputs/10-16.png", width=7.4, height=4.9, dpi=145, verbose=False)

# The quartiles behind the boxes
quartiles = (
    df.groupby("region")["saving"]
    .quantile([0.25, 0.5, 0.75])
    .unstack()
)
print(quartiles.to_string())

# Facets repeat a plot for each region
p = (
    pn.ggplot(
        df,
        pn.aes("income", "saving")
    )
    + pn.geom_point(alpha=0.6)
    + pn.facet_wrap(
        "~region", ncol=2
    )
)
p

p.save("outputs/10-18.png", width=7.4, height=4.9, dpi=145, verbose=False)

# The same facet works with a histogram
p = (
    pn.ggplot(df, pn.aes("saving"))
    + pn.geom_histogram(
        binwidth=250,
        fill="#245b78", color="white"
    )
    + pn.facet_wrap(
        "~region", ncol=2
    )
)
p

p.save("outputs/10-19.png", width=7.4, height=4.9, dpi=145, verbose=False)

# Exercise 2: income per person
print(df["income_per_person"].head(3))
# Plot a histogram of income_per_person.
# Use a bin width of 200 EUR.
# Draw one panel per region, in two columns.
# Keep the same bin width and axes across panels.

# Exercise 2: worked answer
mapping = pn.aes(
    "income_per_person")
p = pn.ggplot(df, mapping)
p = p + pn.geom_histogram(
    binwidth=200,
    fill="#245b78", color="white")
p = p + pn.facet_wrap(
    "~region", ncol=2)
p

p.save("outputs/10-21.png", width=7.4, height=4.9, dpi=145, verbose=False)

# Saving shares as percentages
rates = df.dropna(subset=["saving_share"]).copy()
rates["saving_pct"] = 100 * rates["saving_share"]
print("Plotted households:", len(rates))
print(rates[["saving_share", "saving_pct"]].head(3).round(2)
      .to_string(index=False))

# A new mapping uses the new units
mapping = pn.aes(
    "income_per_person",
    "saving_pct", color="region")
p = pn.ggplot(rates, mapping)
p = p + pn.geom_point(alpha=0.6)
p = p + pn.labs(
    y="Saving (% of income)")
p

p.save("outputs/10-23.png", width=7.4, height=4.9, dpi=145, verbose=False)

# A categorical household size
df["size_group"] = (
    df["size"].astype("category")
)
p = (
    pn.ggplot(
        df, pn.aes(
            "size_group", "saving"
        )
    )
    + pn.geom_boxplot()
)
p

p.save("outputs/10-24.png", width=7.4, height=4.9, dpi=145, verbose=False)

# Mappings can belong to one layer
p = (
    pn.ggplot(
        df,
        pn.aes("income", "saving")
    )
    + pn.geom_hline(yintercept=0)
    + pn.geom_point(
        pn.aes(color="region"),
        alpha=0.6
    )
)
p

p.save("outputs/10-25.png", width=7.4, height=4.9, dpi=145, verbose=False)
