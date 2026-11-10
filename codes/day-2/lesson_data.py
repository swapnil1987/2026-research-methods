"""Prepared classroom sample, reproducing the operations in Lecture 8."""
from pathlib import Path
import pandas as pd

def load_households():
    """Return 195 synthetic households with derived columns and region names."""
    folder=Path(__file__).resolve().parent/"data/raw"
    raw=pd.read_csv(folder/"households.csv")
    clean=raw.drop_duplicates().copy()
    clean["income"]=pd.to_numeric(clean["income"],errors="coerce")
    clean=clean.dropna(subset=["income","consumption"]).copy()
    assert clean["household_id"].is_unique
    assert (clean["size"]>0).all()
    assert (clean[["income","consumption"]]>=0).all().all()
    clean["saving"]=clean["income"]-clean["consumption"]
    clean["income_per_person"]=clean["income"]/clean["size"]
    positive_income=clean["income"].where(clean["income"]>0)
    clean["saving_share"]=clean["saving"]/positive_income
    regions=pd.read_csv(folder/"regions.csv")
    result=clean.merge(regions,on="region_code",how="left",validate="many_to_one")
    assert len(result)==len(clean)
    assert result["region"].notna().all()
    return result
