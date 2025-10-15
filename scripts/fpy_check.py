
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "Fact_TestResults.csv", parse_dates=["timestamp"])

# derive first-pass per unit: unit passes if all rows for that unit are pass==True
unit_pass = (df.groupby("unit_id")["pass"].all()
             .reset_index(name="first_pass"))
units_per_day = (df.assign(day=df["timestamp"].dt.date)
                   .merge(unit_pass, on="unit_id")
                   .groupby("day")
                   .agg(units=("unit_id","nunique"),
                        fpy=("first_pass", "mean"))
                   .reset_index())
print(units_per_day.head(10).to_string(index=False))
