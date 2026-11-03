# Getting a project running

This folder is the **project root for the first lesson**. It is inside the course
repository at `codes/lecture-1/`. The lesson uses only the Python standard library;
JupyterLab is needed to open the notebook.

## Open the starter project

Complete the instructor's environment setup before class. From the course
repository root, open a terminal in the prepared environment and run:

```bash
conda activate research-methods
cd codes/lecture-1
python --version
python household_saving.py
jupyter lab
```

If you received this folder on its own, open a terminal in this folder and skip
the `cd codes/lecture-1` line. Leave the terminal running while using JupyterLab.
Installation is preparation, not part of the one-hour class exercise.

In JupyterLab, double-click `household_saving.py` to open its text editor, or
`project_running.ipynb` to open the notebook. Use **File → New → Terminal** for
shell commands. Check that the terminal is in this starter folder before running
the script. A local browser page is the interface to JupyterLab; it does not by
itself upload the project to a website.

## Check the first result

```text
Monthly saving (EUR): 200
```

The synthetic household receives EUR 1,000 and consumes EUR 800 per month.
Saving is income minus consumption. The script contains those two inputs
directly; it does **not** read the CSV yet.

Change income to `1200`, save the script, and run it again. Predict `400` before
you run it. Restore income to `1000` afterwards.

## Find a file using a relative path

From the starter project root, the supplied data file is
`data/raw/households.csv`. The same file is `raw/households.csv` when the working
folder is `data/`, or `../data/raw/households.csv` when it is `outputs/`.

The notebook displays `Path.cwd()` and checks the root-relative path with
`Path("data/raw/households.csv").is_file()`. Expected result: `True`.
The path is relative to the **current working folder**. It is not automatically
relative to the script's location.

The CSV is a hand-constructed teaching fixture: four synthetic households,
one observation per household, survey year 2026. Income and consumption are
EUR per month; household size is persons; employed is a synthetic 0/1 indicator.
It describes no real population. We locate the file in this block and load it
with pandas in a later block.

## Observe notebook state

1. Run the notebook from top to bottom. Saving should be `200`.
2. Change the income input from `1000` to `1200` and run **only the input cell**.
3. Run **only the display cell**, skipping the calculation cell. It still prints
   `200`: the earlier value of `saving` remains in the kernel.
4. Predict the result of a complete rerun: `400`.
5. Use **Kernel → Restart Kernel and Run All Cells…**, confirm, and check `400`.
6. Restore income to `1000`, restart and run all again, then save the notebook.

The exact menu wording may vary slightly by JupyterLab version. Choose the action
that both restarts the kernel and runs every cell in order. Saved output is a
record of an earlier run; reopening a notebook does not recreate its variables.

## Short agent demonstration

Ask the supported classroom agent to edit **only** `household_saving.py`:

> For the positive income already supplied, append a calculation of saving as
> a share of income: saving / income. Keep the existing inputs and saving output.
> Print the new share with a clear label. Do not read or write files, install
> packages, or change any other file. Show the proposed change and explain it.

Before accepting it, read the change and check the denominator. With income
`1000` and consumption `800`, the share must be `0.2` (20%). With income `2000`
and consumption `1500`, it must be `0.25` (25%). A calculation of `200 / 800`
would answer a different question. Zero-income handling comes in a later block.

Restore the original inputs after the demonstration. A clean restart of the
notebook and a fresh script run should reproduce the baseline saving of `200`.
