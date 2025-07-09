import os
import pandas as pd
import matplotlib.pyplot as plt

# 1) read in the files
macro = pd.read_csv("data/bgd_macro_annual_2023_2025.csv", parse_dates=["year"])
sent  = pd.read_csv("data/sentiment_annual_2023_2025.csv", parse_dates=["year"])

# 2) merge
df = pd.merge(macro, sent, on="year")

# 3) save merged
os.makedirs("data", exist_ok=True)
df.to_csv("data/bgd_combined_annual_2023_2025.csv", index=False)
print("Merged data saved.")

# 4) plot
fig, ax1 = plt.subplots()
ax1.plot(df.year, df.gdp_growth_ann_pct, 'o-', label="GDP Growth")
ax1.plot(df.year, df.inflation_ann_pct, 's-', label="Inflation")
ax1.set_xlabel("Year")
ax1.set_ylabel("Forecast (%)")
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(df.year, df.avg_sentiment_score, '^-', label="Sentiment", color="green")
ax2.set_ylabel("Sentiment Score")

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc="best")

plt.title("Bangladesh (2023–2025): Forecasts vs Sentiment")
plt.tight_layout()

os.makedirs("output", exist_ok=True)
plt.savefig("output/sentiment_vs_macro_2023_2025.png")
plt.show()
