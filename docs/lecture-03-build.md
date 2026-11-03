# Lecture 3 — Conditions, loops and functions

Created on 3 November 2026 in the course checkout, based on commit
`b9b477f6efd48bb82a5e8b3a7062c6043f3da8aa`. These are teaching sources for
the remaining two-hour Day 1 block. The integrating agent handles project
configuration, browser rendering, README links, commits, and publication.

## Delivered sources

- `slides/lecture-03.qmd`: 39 slides, including the title, with contiguous
  speaker-note intervals from 00:00 to 120:00 (minutes:seconds).
- `codes/lecture-3/control_flow.ipynb`: 37 executable code cells, supplied
  without saved outputs. The deliberate ValueError is displayed as Markdown.
- `codes/lecture-3/control_flow.py`: importable worked functions and a guarded
  demonstration using only Python's built-in tools.
- `codes/lecture-3/README.md`: student setup, expected outputs, practice checks,
  explicit function contracts and official Python 3.12 references.

The sources inherit the existing course template and use
`theme/basic-python.css` for 30-pixel code. The shared theme and configuration
were not changed by this deck's author. There are four larger practice tasks,
an additional running-total prediction activity, and worked answers. Every
content slide includes Python code. All household data are synthetic and
amounts are EUR per month; no external data, packages or random seed are used.

## Function contract

`saving_share(income, consumption)` assumes numeric, finite amounts. Negative
income or negative consumption raises
`ValueError("Amounts must be non-negative")`; zero income returns `None`;
positive income returns `(income - consumption) / income`. Negative saving
is valid. Validation precedes the zero-income check. This contract was
coordinated with the errors-and-checks lecture.

The notebook explicitly distinguishes a valid zero share from an undefined
share and checks for `None` before percentage formatting. Paired-list examples
state the alignment assumption and explain that `zip` stops at the shorter
input. The first paired-list demonstration checks list lengths before looping.

## Completed verification

Used Python 3.12.16 and the registered `research-methods` kernel.

- All 38 slide Python blocks were executed against their stated output, with
  one expected ValueError checked separately.
- All 37 notebook code cells executed in a fresh Jupyter kernel without errors.
  The notebook was copied in memory for execution; the distributed file remains
  unexecuted. The executed copy is retained in
  `.cache/lecture-03/executed.ipynb`.
- The worked script's complete run ends with rates `20.0%`, `undefined`, and
  `25.0%`.
- Function checks covered ordinary saving, exact zero saving, negative saving,
  zero income with positive and zero consumption, and four negative-input
  combinations. Negative consumption at zero income correctly raises an error.
- Income-per-person checks covered valid input, zero and negative household
  size, and negative income.
- All 39 clock intervals were checked for adjacency and duration; total 120
  minutes including exercises and debriefs. Breaks are additional.

Local authoring and check evidence are under `.cache/lecture-03/` (ignored).
No project rendering, deployment, commit or push was performed by this deck's
author. The worked rate report uses a full-width loop and explicitly depends
on the earlier saving_share definition. The repeated function-definition cell
was removed from the notebook; the remaining code is unchanged. The integrating
review should inspect the full-width report and longer function/check slides
at classroom size.
