
import pandas as pd
from datetime import datetime

INPUT_CSV  = "data/bb_inflation_monthly_2023_2025.csv"
OUTPUT_CSV = "data/bb_inflation_monthly_2023_2025_manual.csv"


df = pd.read_csv(INPUT_CSV, parse_dates=["date"])


june_dt = pd.to_datetime("2025-06-01")
override_ptp  = 8.48
override_ma12 = None   


mask = df["date"] == june_dt

if mask.any():
    
    df.loc[mask, "ptp_inflation_pct"] = override_ptp
    if override_ma12 is not None:
        df.loc[mask, "ma12_inflation_pct"] = override_ma12
    print(f"🔧 Overrode June 2025 PTP to {override_ptp}")
else:
    
    new_row = {
        "date": june_dt,
        "ptp_inflation_pct": override_ptp,
        "ma12_inflation_pct": override_ma12 or pd.NA
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    print(f" Appended June 2025 with PTP={override_ptp}")


df = df.sort_values("date").reset_index(drop=True)
df.to_csv(OUTPUT_CSV, index=False)
print(f" Saved manual override CSV → {OUTPUT_CSV}")
