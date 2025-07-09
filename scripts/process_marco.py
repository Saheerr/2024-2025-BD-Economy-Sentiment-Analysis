import os
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/bgd_macro_annual_2023_2025.csv", parse_dates=["year"])

df["year"] = pd.to_datetime(df["year"], format="%Y")


fig, ax = plt.subplots()
ax.plot(df["year"], df["gdp_growth_ann_pct"], "o-", label="GDP growth")
ax.plot(df["year"], df["inflation_ann_pct"],   "s-", label="Inflation")


ax.axvline(pd.to_datetime("2024-08-01"), linestyle="--", label="Interim govt (Aug 2024)")


ax.set_xticks(df["year"])
ax.set_xticklabels(df["year"].dt.year)

ax.set_xlabel("Year")
ax.set_ylabel("Percent")
ax.legend()
plt.tight_layout()


os.makedirs("output", exist_ok=True)
plt.savefig("output/gdp_inflation_2023_2025.png")
plt.show()
