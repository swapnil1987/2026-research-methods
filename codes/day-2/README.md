# Day 2: data science and presenting results

Open the notebook for the current lecture in JupyterLab. Run from this folder,
with data/ beside the notebooks.

| Lecture | Notebook | Worked script |
|---|---|---|
| 7. Pandas basics | [01_pandas.ipynb](01_pandas.ipynb) | [01_pandas.py](01_pandas.py) |
| 8. Preparing data | [02_preparing.ipynb](02_preparing.ipynb) | [02_preparing.py](02_preparing.py) |
| 9. Grouped summaries and joins | [03_summaries.ipynb](03_summaries.ipynb) | [03_summaries.py](03_summaries.py) |
| 10. Grammar of graphics with plotnine | [04_grammar.ipynb](04_grammar.ipynb) | [04_grammar.py](04_grammar.py) |
| 11. Figure design | [05_design.ipynb](05_design.ipynb) | [05_design.py](05_design.py) |
| 12. Tables and a research report | [06_tables.ipynb](06_tables.ipynb) | [06_tables.py](06_tables.py) |

The notebooks contain classroom exercises followed by worked answers.
Try each exercise before opening its worked answer.

## Start

Create the environment from environment-student.yml, or add plotnine to your
existing course environment:

    conda install -n research-methods -c conda-forge "plotnine>=0.15,<0.16"
    conda activate research-methods

From this folder, run:

    jupyter lab

Choose the research-methods kernel. For a worked script, run for example:

    python 04_grammar.py

Figures, tables, and other generated files go in outputs/.

## Data

All households are invented. Income, consumption, and saving are EUR per month.
See [the input description](data/README.md). Lecture 7 starts with a small
hand-checkable table. Lecture 8 prepares the CSV sample. Later lectures reuse
those preparation steps through [lesson_data.py](lesson_data.py).

## References

- [pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [plotnine aesthetic mappings](https://plotnine.org/guide/aesthetic-mappings.html)
- [plotnine reference](https://plotnine.org/reference/)
