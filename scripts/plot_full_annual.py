import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/bgd_full_annual_2023_2025.csv", parse_dates=["year"])
df["year"] = df["year"].dt.year

fig, ax1 = plt.subplots(figsize=(8,5))
ax1.plot(df.year, df.gdp_growth_ann_pct, marker="o", label="GDP Growth")
ax1.plot(df.year, df.inf_ptp_ann_avg_pct,  marker="s", label="Avg PTP Inflation")
ax1.set_ylabel("Percent")
ax1.set_xlabel("Year")
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(df.year, df.avg_sentiment_score, marker="^", color="tab:green", label="Avg Sentiment")
ax2.set_ylabel("Sentiment (–1 to +1)")


l1, lab1 = ax1.get_legend_handles_labels()
l2, lab2 = ax2.get_legend_handles_labels()
ax1.legend(l1+l2, lab1+lab2, loc="upper left")

plt.title("Bangladesh 2023–2025: GDP, Inflation & News Sentiment")
plt.tight_layout()
plt.savefig("output/full_annual_comparison.png")
plt.show()
