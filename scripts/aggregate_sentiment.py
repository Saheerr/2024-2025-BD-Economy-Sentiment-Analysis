import os
import sys
import pandas as pd

input_file = "data/bangladesh_econ_news_2023_2025.csv"
output_file = "data/sentiment_annual_2023_2025.csv"
years = [2023, 2024, 2025]

if not os.path.exists(input_file):
    print(f"Error: '{input_file}' not found.")
    sys.exit(1)

df = pd.read_csv(input_file)

if "publish_date" not in df or "sentiment" not in df:
    print("Error: expected columns 'publish_date' and 'sentiment'.")
    print("Found:", df.columns.tolist())
    sys.exit(1)

df["publish_date"] = pd.to_datetime(df["publish_date"])
df["score"] = df["sentiment"].str.lower().map({"positive": 1, "neutral": 0, "negative": -1})
df["year"] = df["publish_date"].dt.year

annual = (
    df[df["year"].isin(years)]
    .groupby("year", as_index=False)["score"]
    .mean()
)
annual.columns = ["year", "avg_sentiment_score"]

os.makedirs(os.path.dirname(output_file), exist_ok=True)
annual.to_csv(output_file, index=False)

print("Annual sentiment saved to", output_file)
print(annual)
