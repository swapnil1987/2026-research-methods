# Day 2 teaching materials

Day 2 follows the six-lecture structure used for Day 1. Each lecture has its
own HTML deck, notebook, and worked script. The Day 2 URL is a contents page.

| Lecture | Topic | Slides | Minutes | Code cells |
|---|---|---:|---:|---:|
| 7 | Pandas basics | 23 | 60 | 22 |
| 8 | Preparing data | 24 | 60 | 23 |
| 9 | Grouped summaries and joins | 25 | 60 | 24 |
| 10 | Grammar of graphics with plotnine | 26 | 75 | 25 |
| 11 | Figure design | 24 | 60 | 23 |
| 12 | Tables and a research report | 21 | 45 | 20 |
| Total | | 143 | 360 | 137 |

All 137 teaching slides contain Python examples or exercise starters, with
actual calculated output, tables, or plots where relevant. Each lecture has two
exercises followed by worked answers. Small tables introduce operations before
the larger synthetic household CSV. Plotting examples put code beside charts.

## Build

Use Quarto 1.9.38 in the declared course environment, or the documented compatible
topics-econometrics environment:

    XDG_CACHE_HOME=/tmp/research-methods-quarto-cache RESEARCH_METHODS_ENV=topics-econometrics bash scripts/render-slides.sh
    python3 scripts/package-student-kit.py
    python3 scripts/package-day-2.py

The shared course theme and 30px code style match Day 1. The contents page has a
single-column lecture list on narrow screens. Generated artifacts remain under
ignored paths.

## Runtime verification

The six distributed notebooks have no saved execution output. Copies ran from
fresh research-methods kernels with Python 3.12, pandas 3.1, and plotnine 0.15.9.
All six matching Python scripts executed successfully. The final shortened
grammar examples were checked again after layout corrections.

Raw CSV hashes remain unchanged. The shared lesson_data.py loader reconstructs
195 complete monetary records from 201 input rows, preserving zero incomes.
193 saving shares have positive denominators. Lecture 8 teaches those operations
explicitly; later notebooks can run independently using the loader.

The runtime download contains 19 explicitly listed files: six notebooks, six
scripts, a shared loader, raw data and documentation, output-folder README, and
the student environment specification. It contains no slides, executed outputs,
private files, or unrelated notebooks.

## Review

Independent source review checked examples, exercise/answer agreement, grouping
and join cardinality, denominators, chart statistics, and formatting precision.
It corrected missing requested chart labels, a sample comparison, output
columns, and timing notes.

Every slide was inspected through rendered contact sheets, with full-size
inspection of dense examples, code beside charts, and the HTML table. Browser
checks covered all 143 slides at 1600x900, landscape phone widths, fragments,
navigation, overview, slide/footer bounds, and horizontal and vertical code
clipping inside containers. The contents page was checked at 1600x900 and
390x844, including its six lecture links and readable stacked mobile layout.
Code lines were shortened instead of reducing the template's font size.

Local QA evidence is in .cache/day-02-revision/. The final release is built from
a clean export of its Git commit, then checked through GitHub Actions and live
Pages routes.
