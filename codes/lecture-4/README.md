# Reading errors and checking calculations — Lecture 4

Use the existing `research-methods` environment. From the course repository root:

```bash
conda activate research-methods
cd codes/lecture-4
jupyter lab
```

Open `checking_calculations.ipynb`, select the course's Python kernel, and run
cells with **Shift + Enter**. If JupyterLab is already open at the repository
root, navigate to this folder in its file browser. If you downloaded the files
separately, open a terminal in their folder and skip `cd codes/lecture-4`.

The notebook follows the slides. Predict each result, attempt the exercises,
then compare with the worked repairs. Deliberately failing snippets are
displayed as Markdown rather than executable cells. You can copy one into an
extra scratch cell to reproduce the error; remove that scratch cell before
restarting and running all cells. No extra packages or data files are required.

These are classroom exercises with visible answers, separate from the graded
take-home task. All household amounts are synthetic EUR per month.

## Run the worked checks

```bash
python checking_calculations.py
```

Expected output:

```text
Saving amount checks passed
Saving share checks passed
Invalid input rejected: Amounts must be non-negative
Fresh calculation (EUR/month): 400
```

The final `try`/`except` block in the script checks an expected rejection while
allowing the script to continue. It is supplied verification code; students
do not need to write an exception handler to complete the classroom exercises.

## The function contract

`saving_share(income, consumption)` assumes finite numeric monthly amounts in
the same currency. For this teaching specification:

- Negative income or consumption raises `ValueError`.
- Zero income returns `None`, because its saving share is undefined.
- Otherwise it returns `(income - consumption) / income`.
- Consumption above income can produce a valid negative saving amount or share.

The input restriction is a classroom specification, not a general claim that
negative income is invalid in every real dataset. This function is not a full
data-validation system.

## When a check fails

1. Record the inputs, expected answer and actual result or error.
2. Read the last exception line, then locate the relevant source line.
3. Inspect the values and their types; reduce the problem if necessary.
4. Change the cause, rerun the same case, then rerun the other relevant cases.
5. Restart the notebook kernel and run all cells in order.

Assertions are development checks. Use explicit `if`/`raise` logic for required
input validation. A clean run and passing examples provide evidence for the
cases checked; use hand calculations, units and the task definition as well.

## References

- [Python 3.12: errors and exceptions](https://docs.python.org/3.12/tutorial/errors.html)
- [The assert statement](https://docs.python.org/3.12/reference/simple_stmts.html#the-assert-statement)
- [math.isclose](https://docs.python.org/3.12/library/math.html#math.isclose)
