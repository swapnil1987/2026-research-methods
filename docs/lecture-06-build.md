# Lecture 6 — First look at a dataset

Teaching sources and deterministic checks prepared on 3 November 2026 for the
one-hour final block of Day 1. Rendering and publication are handled with the
other Day 1 lectures by the repository's course release workflow.

## Material

- `slides/lecture-06.qmd`: **26 slides**, with a speaker-note clock on every
  slide, including the title. Intervals are contiguous from 00:00 to 60:00
  (minutes:seconds); exercises and debriefs are included.
- `codes/lecture-6/first_dataset.ipynb`: **24 code cells**, supplied without
  execution counts or saved output. It follows the slides and includes a
  worked answer after the final classroom practice task.
- `codes/lecture-6/first_dataset.py`: runnable worked analysis and checked
  export, using the existing pandas installation.
- Student instructions, a data dictionary, and an `outputs/` folder README.
- `codes/lecture-6/data/raw/households.csv`: byte-identical copy of the four
  synthetic records already used in Lecture 1. One household per row, survey
  year 2026; amounts are EUR per month. No real people are represented.

The lecture covers CSV structure, observation units, relative paths,
`read_csv`, inspecting rows, shape, names and types, selecting columns and row
positions, Boolean row selection, simple derived columns, hand checks, missing
inputs and unique IDs, summaries, and a clean CSV export/read-back. It inherits
the course template and `theme/basic-python.css`; code is sized at 30 pixels.

## Deterministic verification

Checks used **Python 3.12.16**, **pandas 3.1.0**, and the existing
`research-methods` environment. All **23 Python slide blocks** were executed
in lesson order in an isolated temporary folder. Every displayed output
matched the executed output, including table alignment and dtype labels.

All **24 notebook code cells** executed in a fresh `research-methods` Jupyter
kernel without errors. Both the notebook and standalone script were run
against temporary copies of the input so verification did not overwrite a
student's existing output. Each produced a derived CSV with four rows and two
columns, `household_id` and `saving_eur_month`.

Expected results were checked explicitly:

```text
Rows and columns: (4, 6)
Saving by household: [200, 400, 500, -50]
Negative-saving household IDs: [4]
Total saving: 1050.00 EUR/month
Mean saving: 262.50 EUR/household/month
Saved and checked: outputs/household_saving.csv
```

The input fixture, its Lecture 1 original, and the temporary test copy were
unchanged after execution. Their SHA-256 is:

```text
36dce5407c2760f1823d0d3d6d4b846001e7403c14a629c1d42aef1172e8a664
```

Local evidence is under `.cache/lecture-06/`: `slide-output-checks.json`,
`runtime-checks.json`, and the executed notebook copy `executed.ipynb`. These
are ignored by Git. The distributed notebook remains unexecuted.

## Reproduce

From the course repository root, to run the worked example:

```bash
conda activate research-methods
cd codes/lecture-6
python first_dataset.py
```

Open the notebook with `jupyter lab` from that same folder and choose
**Kernel → Restart Kernel and Run All Cells…**. Derived files go to `outputs/`;
the raw file is preserved.

The release coordinator renders and visually checks the deck with the other
Day 1 materials. No separate project render or publication was performed by
this lecture's worker.
