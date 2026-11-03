# First look at a dataset — Lecture 6

This one-hour lesson reads the same four synthetic households introduced in
Lecture 1. Each record is a household in survey year 2026. Income, consumption,
and saving are EUR per month; household size is persons. `employed` is an
invented 0/1 teaching indicator. The records represent no real population.

## Open the lesson

From the course repository root, in a terminal:

```bash
conda activate research-methods
cd codes/lecture-6
jupyter lab
```

Open `first_dataset.ipynb`. Work from top to bottom; earlier setup cells create
the `households` input table and later cells create a separate `analysis` table.
The notebook contains classroom practice and worked answers, not the graded
take-home task. Use the Python kernel from the course environment.

If using a standalone download, keep `first_dataset.ipynb`, `first_dataset.py`,
and `data/raw/households.csv` in this folder structure. Open a terminal here,
activate the environment and run `jupyter lab`; skip the repository-relative
`cd` command. pandas is already included in the course environment.

## Check the calculation

In a terminal in this lesson folder:

```bash
python first_dataset.py
```

Expected results:

```text
Rows and columns: (4, 6)
Saving by household: [200, 400, 500, -50]
Negative-saving household IDs: [4]
Total saving: 1050.00 EUR/month
Mean saving: 262.50 EUR/household/month
Saved and checked: outputs/household_saving.csv
```

The output CSV contains four rows and two columns: `household_id` and
`saving_eur_month`. It is generated in `outputs/`; the raw input is not changed.
These totals describe only this small synthetic fixture. A negative saving
amount is meaningful in the example and must not be deleted to make a check pass.

## Data dictionary

| Column | Meaning |
|---|---|
| `household_id` | Unique integer teaching identifier, not a quantitative outcome |
| `income_eur_month` | Household income, EUR per month |
| `consumption_eur_month` | Household consumption, EUR per month |
| `household_size` | Number of persons in the household |
| `employed` | Synthetic 0/1 indicator used to practise selection |
| `survey_year` | 2026 for all four records |

The CSV is a byte-identical copy of `codes/lecture-1/data/raw/households.csv`.
No missing cells or duplicate identifiers have been inserted. Later lessons
will teach how to investigate such problems in other inputs.

## References

- [pandas: reading and writing tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
- [Selecting rows and columns](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)
- [Calculating new columns](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
