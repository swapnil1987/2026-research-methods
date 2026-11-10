"""Synthetic Day 2 fixture. Python random seed 20261111."""
from pathlib import Path
import csv
import random
root=Path(__file__).resolve().parents[1]/"codes/day-2/data/raw"
root.mkdir(parents=True,exist_ok=True)
rng=random.Random(20261111)
rows=[]
for i in range(200):
    size=1+i%5
    income=300+rng.randrange(300,1601)*size
    consumption=max(0,round(income*rng.uniform(.65,1.12)/10)*10)
    rows.append([f"H{i+1:03}",str(income),consumption,size,["N","S","E","W"][i%4]])
for i in (12,42):
    rows[i][1]="0"
rows[7][1]="missing"
rows[22][1]=""
for i in (31,67,101):
    rows[i][2]=""
rows.append(rows[0].copy())
with (root/"households.csv").open("w",newline="") as f:
    w=csv.writer(f, lineterminator="\n")
    w.writerow(["household_id","income","consumption","size","region_code"])
    w.writerows(rows)
with (root/"regions.csv").open("w",newline="") as f:
    w=csv.writer(f, lineterminator="\n")
    w.writerow(["region_code","region"])
    w.writerows([["N","North"],["S","South"],["E","East"],["W","West"]])
