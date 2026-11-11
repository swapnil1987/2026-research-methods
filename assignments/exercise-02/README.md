# Coding Assignment 2

[Open the assignment (PDF)](assignment-02.pdf)

Open your pull request by **Monday, 16 November 2026 at 23:59 Vilnius time**.

Download the two inputs and save them in a folder called `data` beside your notebook. Both links point to the same fixed version of the data. Keep the flights file zipped. If the airline lookup opens in a browser tab, save the page as `airlines.csv`.

- [Download flights.csv.zip (7.9 MiB)](https://raw.githubusercontent.com/machow/nycflights13-py/1d40369400d77379a78641afd119fc302a5a9659/nycflights13/data/flights.csv.zip)
- [Download airlines.csv](https://raw.githubusercontent.com/machow/nycflights13-py/1d40369400d77379a78641afd119fc302a5a9659/nycflights13/data/airlines.csv)

```python
import pandas as pd

flights = pd.read_csv("data/flights.csv.zip")
airlines = pd.read_csv("data/airlines.csv")
```

The U.S. Bureau of Transportation Statistics collected the flight records. Hadley Wickham's *nycflights13* documents the data and distributes them under CC0. The downloads are Michael Chow's CSV version. [Flight variables](https://nycflights13.tidyverse.org/reference/flights.html) · [Airline codes](https://nycflights13.tidyverse.org/reference/airlines.html)
