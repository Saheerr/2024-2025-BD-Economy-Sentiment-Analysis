import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("bangladesh_econ_news_2023_2025.csv", parse_dates=["publish_date"])


summary_counts = df.groupby(["period", "sentiment"]).size().unstack(fill_value=0)
summary_props  = summary_counts.div(summary_counts.sum(axis=1), axis=0)


periods = ["Pre-August-2024", "Post-August-2024", "2025"]
summary_counts = summary_counts.reindex(periods)
summary_props  = summary_props.reindex(periods)


x = np.arange(len(periods))
width = 0.25

plt.figure(figsize=(8,5))
for i, s in enumerate(summary_counts.columns):
    plt.bar(x + i*width, summary_counts[s], width, label=s)
plt.xticks(x + width, periods)
plt.title("News Sentiment Counts by Period (Jan 2023–Jul 2025)")
plt.ylabel("Number of Headlines")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/sentiment_counts_by_period.png", dpi=300)
plt.show()


plt.figure(figsize=(8,5))
for i, s in enumerate(summary_props.columns):
    plt.bar(x + i*width, summary_props[s], width, label=s)
plt.xticks(x + width, periods)
plt.title("News Sentiment Proportions by Period (Jan 2023–Jul 2025)")
plt.ylabel("Proportion of Headlines")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/sentiment_proportions_by_period.png", dpi=300)
plt.show()
