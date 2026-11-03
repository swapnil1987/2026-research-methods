# Basic Python — Lecture 2

This two-hour lesson follows Getting a project running. It covers variables,
arithmetic, numeric types, strings, conversions, formatted output, comparisons,
Boolean combinations, lists, indexing, slicing, and simple summaries. All
household examples are synthetic; amounts are EUR per month.

## Follow the lesson

If you have the full course repository, the files are already in this folder.
If you downloaded only the first lesson's starter project, open
[`basic_python.ipynb`](basic_python.ipynb) and
[`basic_python.py`](basic_python.py) on GitHub and use **Download raw file** for
each. Save both files in a new local `lecture-2` folder, keeping their original
filenames. You can use these files before learning Git commands.

Use the existing `research-methods` environment. From the course repository root:

```bash
conda activate research-methods
cd codes/lecture-2
jupyter lab
```

For a standalone downloaded folder, open a terminal in that folder, activate
the environment, and run `jupyter lab`; skip the `cd codes/lecture-2` command.

Open `basic_python.ipynb`, select the course's Python kernel, and press
**Shift + Enter** to run each code cell. If JupyterLab is already open at the
repository root, open this folder in its file browser instead. If it is open
inside the first lesson's folder, start a new session at the repository root or
this folder. No new packages or data downloads are needed.

The notebook follows the slides and includes classroom exercises with visible
worked answers. Predict the output before running code and attempt each
exercise before reading its answer. The deliberate type error is displayed in
a Markdown cell so it does not interrupt a complete notebook run. Use an extra
scratch cell if you want to reproduce that error yourself.

This is practice material. The graded take-home exercise will have its own task
sheet, rubric, and pull-request submission instructions.

## Run the worked script

In a terminal in this folder:

```bash
python basic_python.py
```

The first line should report saving of `200`. The script finishes with:

```text
HH04: saving = 300.00 EUR/month
Saving rate = 20.0%
Income per person = 500.00 EUR/month
Non-negative saving: True
```

Change the final household's consumption to `1600`, save, and run again. Saving
becomes `-100.00`, its share is displayed as `-6.7%`, income per person stays
`500.00`, and the non-negative check becomes `False`.

## Check your classroom exercises

1. **One household:** income `1250`, consumption `1000`, size `2` give saving
   `250`, saving share `0.2`, and income per person `625.0`.
2. **Numeric text:** converting `"1200"` with `float` before adding `100` gives
   `1300.0`. Converting with `int` is also valid for that input and gives `1300`.
3. **Stored Boolean:** the eligibility example prints `True` twice until the
   comparison is recalculated after changing income to `1201`; it then gives
   `False`.
4. **Lists:** selecting first, last and first two gives `1000`, `800`, and
   `[1000, 1200]`. After replacing the third item and appending, the list is
   `[1000, 1200, 900, 1500]`; count `4`, total `4600`, mean `1150.0`.
5. **Household report:** use the four-line script output above, then check the
   changed-consumption case by hand.

Restart the notebook kernel and run all cells in order before sharing your
work. A saved output can be stale. A clean run checks execution order; hand
calculations and units check whether the formula answers the intended question.

## References

- [Python 3.12: numbers, text and lists](https://docs.python.org/3.12/tutorial/introduction.html)
- [List operations](https://docs.python.org/3.12/tutorial/datastructures.html#more-on-lists)
- [Comparisons and Boolean operations](https://docs.python.org/3.12/library/stdtypes.html#comparisons)
- [Formatted output](https://docs.python.org/3.12/tutorial/inputoutput.html#formatted-string-literals)
- [Floating-point representation](https://docs.python.org/3.12/tutorial/floatingpoint.html)
