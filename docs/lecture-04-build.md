# Lecture 4 — Reading errors and checking calculations

Prepared on 3 November 2026 against course commit
`b9b477f6efd48bb82a5e8b3a7062c6043f3da8aa`. This lesson is included in the
Day 1 course release. See [integrated build checks](day-1-build.md) for rendering
and visual verification.

## Material

- `slides/lecture-04.qmd`: 25 slides, including the title, with contiguous
  speaker-note timing from 00:00 to 60:00 (minutes:seconds).
- `codes/lecture-4/checking_calculations.ipynb`: 20 code cells, supplied
  unexecuted and without saved output. Deliberately failing examples are
  Markdown. Practice answers are visible because this is classroom material.
- `codes/lecture-4/checking_calculations.py`: a readable worked script with
  hand checks, float comparisons, boundary checks and an expected rejection.
- `codes/lecture-4/README.md`: launch instructions, expected script output,
  the function contract, a repair workflow and official Python 3.12 references.

The lesson inherits the course Reveal template and uses the existing
`theme/basic-python.css` for 30-pixel code. No shared theme, project
configuration, top-level README or existing lesson files were changed.

Topics include traceback reading, small reproducible examples, syntax and
indentation, common runtime exception types, wrong-but-running formulas,
hand-worked cases, assertions, `math.isclose`, edge cases, a supplied agent
change and clean reruns.

## Shared function contract

The `saving_share(income, consumption)` interface matches Lecture 3. Inputs
are finite numeric monthly amounts in the same currency. Negative income or
consumption raises `ValueError("Amounts must be non-negative")`; zero income
returns `None`; other valid inputs return `(income - consumption) / income`.
Consumption above income can produce valid negative saving. Comprehensive
type and data validation is outside this small teaching function's scope.

## Checks

Verification used Python 3.12.16 in `research-methods`:

```bash
~/miniconda3/envs/research-methods/bin/python \
  .cache/lecture-04/check_examples.py
```

All 30 slide Python blocks were checked, including 13 deliberate failures with
their expected exception types. Displayed calculation results agree with
execution. The check also verifies all 25 timing intervals, their 60-minute
total, the worked script's four output lines, and positive/negative-saving,
zero-income and invalid-input cases for `saving_share`.

All 20 notebook code cells executed without error in a fresh `research-methods`
Jupyter kernel with working directory `codes/lecture-4/`. An executed copy and
the verification reports are retained only under `.cache/lecture-04/`.
The distributed notebook remains unexecuted. No external packages, datasets
or external coding agent were required for the examples.

The shortened traceback example now computes `saving` before dividing. Its
verified call frame is `analysis.py`, line 5, and its failing division frame is
line 3. The displayed source uses at most 33 characters per line and the
shortened traceback at most 35. The notebook mirrors both snippets, and its
20 code cells were rechecked successfully after this revision.

Visual review identified a clipped return expression in the two-column
traceback slide. Splitting the calculation and updating both frame numbers
fixed it. The repaired slide and exercise/answer spacing were inspected at the
course's 1600 × 900 slide size.
