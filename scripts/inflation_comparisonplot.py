
import os
import pandas as pd
import matplotlib.pyplot as plt


ANNUAL_CSV = "data/bgd_combined_annual_2023_2025.csv"
MONTHLY_CSV = "data/bb_inflation_monthly_2023_2025_manual.csv"
OUTPUT_DIR = "output"


os.makedirs(OUTPUT_DIR, exist_ok=True)

#  annual inflation

df_annual = pd.read_csv(ANNUAL_CSV, parse_dates=["year"])
df_annual["year"] = df_annual["year"].dt.year

plt.figure(figsize=(6,4))
plt.plot(df_annual["year"], df_annual["inflation_ann_pct"], marker="o")
plt.title("Annual Inflation (Actual & Forecast)")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")
plt.grid(True)
plt.tight_layout()
annual_plot = os.path.join(OUTPUT_DIR, "annual_inflation.png")
plt.savefig(annual_plot)
print(f"Saved annual inflation plot to {annual_plot}")
plt.close()

# monthly inflation

df_monthly = pd.read_csv(MONTHLY_CSV, parse_dates=["date"])

plt.figure(figsize=(8,4))
plt.plot(df_monthly["date"], df_monthly["ptp_inflation_pct"], marker="o")
plt.title("Monthly Point-to-Point Inflation (Jan 2023 – Jul 2025)")
plt.xlabel("Date")
plt.ylabel("Inflation (%)")
plt.grid(True)
plt.tight_layout()
monthly_plot = os.path.join(OUTPUT_DIR, "monthly_inflation.png")
plt.savefig(monthly_plot)
print(f"Saved monthly inflation plot to {monthly_plot}")
plt.close()
