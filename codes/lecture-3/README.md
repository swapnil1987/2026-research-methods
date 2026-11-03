# Conditions, loops and functions — Lecture 3

This two-hour classroom lesson follows Basic Python. It uses only Python's
built-in tools; no new packages or datasets are needed. Household amounts are
synthetic and measured in EUR per month.

## Open and run the examples

From the course repository root, in a terminal:

```bash
conda activate research-methods
cd codes/lecture-3
jupyter lab
```

Open `control_flow.ipynb`, choose the course Python kernel, and press **Shift +
Enter** to run each code cell. If JupyterLab is already open at the repository
root, navigate to this folder instead. For a standalone copy of this folder,
open a terminal here, activate the environment, and run `jupyter lab`; skip the
`cd codes/lecture-3` line.

The notebook contains worked examples and four larger practice tasks, plus a
running-total prediction activity. Attempt each task before reading its worked
answer. This is classroom practice, not the graded take-home exercise. The
deliberate `ValueError` example is displayed as Markdown so **Restart Kernel
and Run All Cells** succeeds. Try the deliberate error only in an extra scratch
cell if you want to see its traceback.

Run the worked script from a terminal in this folder:

```bash
python control_flow.py
```

Its last four lines should be:

```text
Saving shares:
Rate: 20.0%
Rate: undefined
Rate: 25.0%
```

If you do not have a clone, open `control_flow.ipynb` and `control_flow.py` on
GitHub and use **Download raw file** for each. Keep their filenames and save
them together in a new local `lecture-3` folder. The files work independently
of the rest of the repository.

## The saving-share contract

`saving_share(income, consumption)` accepts numeric, finite amounts and uses
these classroom rules:

- Negative income **or** negative consumption raises
  `ValueError("Amounts must be non-negative")`.
- Zero income returns `None`, because division by zero does not define a saving
  share. It does not return zero percent.
- Positive income returns `(income - consumption) / income` as a fraction.
- Consumption can exceed income, so negative **saving** and negative saving
  shares are valid results.

Examples: `(1000, 800)` gives `0.2`; `(1000, 1000)` gives `0.0`;
`(1000, 1100)` gives `-0.1`; `(0, 100)` gives `None`. Negative consumption
remains invalid even when income is zero, because validation happens first.

These are declared teaching assumptions. They do not claim that all research
definitions of income must exclude negative values. The introductory function
does not comprehensively validate arbitrary strings, missing values, Boolean
values, infinities, or NaN; real inputs need checks appropriate to the data.

`income_per_person(income, household_size)` in the worked script rejects
negative income and non-positive household size. The first classroom exercise
uses a simpler version with positive-size inputs supplied by the question.

## Check your classroom tasks

1. **Classify saving:** `-50`, `0`, and `200` should give `Negative`, `Zero`,
   and `Positive`, with exactly one label for each amount.
2. **Count and total:** `[200, 0, -50, 300]` contains two positive values,
   totalling `500`. Including zero changes the count to three but not the total.
3. **Income per person:** `(1200, 3)` returns `400.0`; `(1000, 2)` returns
   `500.0`. Store or format the returned value; a function that only prints it
   does not return that number.
4. **Checked rate report:** the three input pairs `(1000, 800)`, `(0, 100)`,
   and `(2000, 1500)` should print `20.0%`, `undefined`, and `25.0%`.

For paired lists, check both their lengths and their household order. `zip`
pairs by position and stops at the shorter input; it does not match household
identifiers. These teaching lists are aligned by construction.

## References

- [Python 3.12: conditions, loops and functions](https://docs.python.org/3.12/tutorial/controlflow.html)
- [Built-in exceptions: ValueError](https://docs.python.org/3.12/library/exceptions.html#ValueError)
