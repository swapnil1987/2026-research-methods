# Coding Assignment 2: What can a traveller learn from a year of flights?

Files:

- `exercise_02.ipynb`: sample checks, airline join, the five-airline table, figure drafts and caption
- `figure.png`: the final figure, saved by the notebook

## Get the data

Create a folder called `data` beside the notebook and download both files into it:

- `flights.csv.zip` (336,776 flights from EWR, JFK and LGA in 2013). Keep it zipped.
- `airlines.csv` (full airline name for each carrier code)

The data come from the U.S. Bureau of Transportation Statistics via Hadley Wickham's
`nycflights13` (CC0). The raw files are not part of this pull request.

## Run

Use the Day 2 environment (`environment-student.yml`: Python 3.12, pandas, plotnine 0.15):

    conda activate research-methods
    jupyter lab

Open `exercise_02.ipynb`, choose the research-methods kernel, then use
Kernel > Restart Kernel and Run All Cells. The notebook prints the table and saves
`figure.png` in this folder.
