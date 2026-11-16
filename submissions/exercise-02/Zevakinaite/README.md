# Exercise 02: Flight delays

## Download the data

Download these two inputs, which point to the same fixed version of the data:

- [flights.csv.zip](https://raw.githubusercontent.com/machow/nycflights13-py/1d40369400d77379a78641afd119fc302a5a9659/nycflights13/data/flights.csv.zip)
- [airlines.csv](https://raw.githubusercontent.com/machow/nycflights13-py/1d40369400d77379a78641afd119fc302a5a9659/nycflights13/data/airlines.csv)

Save both files in a folder called `data` beside `exercise_02.ipynb`. Keep the flights file zipped. If the airline lookup opens in a browser tab, save the page as `airlines.csv` in the `data` folder.

The folder should look like this:

```text
exercise-02/
├── data/
│   ├── airlines.csv
│   └── flights.csv.zip
└── exercise_02.ipynb
```

## Run the notebook

1. Activate the course's Day 2 Python environment. It needs Python, pandas, plotnine, and Jupyter. If `plotnine` is not installed in the active Conda environment, install it with `conda install -c conda-forge plotnine`.
2. Open a terminal in this folder and start JupyterLab:

   ```bash
   jupyter lab
   ```

3. Open `exercise_02.ipynb` and choose the Day 2 environment as its kernel.
4. Restart the kernel and run all cells from top to bottom. The notebook loads the data from `data/` and recreates the table and figure.

## AI-use record

I used ChatGPT to clarify assignment concepts, discuss code and debugging, and review explanations.
