# Day 2: data science and clear research results

Six teaching hours on 11 November 2026, excluding breaks and an individual test.
No prior pandas or plotting knowledge is assumed.

## Setup

Use Python 3.12 and the research-methods environment. New users create the updated
environment-student.yml. Existing users run these commands in a terminal:

    conda install -n research-methods -c conda-forge "plotnine>=0.15,<0.16"
    conda activate research-methods
    python -c "import pandas, plotnine; print(pandas.__version__, plotnine.__version__)"

From the repository root, change to codes/day-2/ and start jupyter lab.
Open data_science.ipynb and select the research-methods kernel. A separately
downloaded folder works if the notebook, script, and data/ folder stay together.
No Git commands are needed. Run python worked_analysis.py from this folder
for the worked script. Outputs go under outputs/. The distributed notebook has
no saved outputs; restart and run all cells to reproduce the lesson.

## Sequence and exercises

Research question 15 minutes; first pandas dataset 55; preparation and checks 50;
summaries and joins 45; grammar of graphics 60; figure design 45; tables 30;
reproducible workflow and classroom lab 60. Total: 360 minutes.
Seven numbered exercises have worked answers. Attempt each before reading its
answer. An additional coding-agent discussion asks for a bounded styling change.
These are classroom materials, separate from graded assignments and test keys.

## Data and analytical choices

See data/README.md. All households and regions are synthetic and unweighted.
The 201 raw rows contain one exact duplicate and five incomplete monetary
records. The declared cleaning policy retains 195 households. Two have zero
income, leaving 193 defined saving shares. The checked region join preserves
195 rows and matches every code. Do not replace undefined shares with zero.
The complete-record policy is a classroom example, not a universal prescription.

The mean household share and pooled share answer different questions. Here the
pooled totals also include consumption of zero-income households. These
descriptive synthetic comparisons do not establish causation or represent
real regional populations.

## Outputs

Figures show distributions, relationships, regional means, and fixed-scale
facets. The script writes PNGs, a PDF, an HTML display table, and unrounded CSV summaries. Plot code
remains editable. Slide images reproduce that code. Preserve original money
units and distinguish fractional shares from percentage displays.
For reproducing slide PNG assets, use each named plot's save method with
width=9, height=4.6, dpi=150; save a vector PDF or SVG for print.

## Primary references

- https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- https://pandas.pydata.org/docs/user_guide/merging.html
- https://plotnine.org/guide/aesthetic-mappings.html
- https://plotnine.org/reference/geom_col.html
- https://plotnine.org/reference/ggplot.html
