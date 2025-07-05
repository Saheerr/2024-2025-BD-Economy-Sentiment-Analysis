import feedparser
import pandas as pd
from datetime import date, timedelta, datetime
from urllib.parse import quote
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def month_windows(start, end):
    curr = date(start.year, start.month, 1)
    while curr <= end:
        nxt = (curr.replace(day=28) + timedelta(days=4)).replace(day=1)
        yield curr, min(end, nxt - timedelta(days=1))
        curr = nxt


START   = date(2023, 1, 1)
END     = date(2025, 7, 4)
CUTOFF  = date(2024, 8, 1)
OUTPUT  = "bangladesh_econ_news_2023_2025.csv"

analyzer = SentimentIntensityAnalyzer()
records  = []
seen_urls = set()

for mn_begin, mn_end in month_windows(START, END):
   
    q = f"Bangladesh economy after:{mn_begin.isoformat()} before:{mn_end.isoformat()}"
    rss_url = "https://news.google.com/rss/search?q=" + quote(q)
    print(f"Fetching {mn_begin}→{mn_end}…", end=" ")
    feed = feedparser.parse(rss_url)
    count = 0

    for e in feed.entries:
        pub = datetime(*e.published_parsed[:6]).date()
        url = e.link
        if url in seen_urls:
            continue
        seen_urls.add(url)

        # sentiment
        comp = analyzer.polarity_scores(e.title)["compound"]
        sent = "Positive" if comp >= 0.05 else "Negative" if comp <= -0.05 else "Neutral"

        # period bucket
        if pub < CUTOFF:
            period = "Pre-August-2024"
        elif pub.year == 2024:
            period = "Post-August-2024"
        else:
            period = "2025"

        records.append({
            "title":        e.title,
            "url":          url,
            "publish_date": pub,
            "period":       period,
            "sentiment":    sent
        })
        count += 1

    print(f"{count} items")


df = pd.DataFrame(records)
df.to_csv(OUTPUT, index=False)
print(f"\n✅ Saved {len(df)} headlines to {OUTPUT}")


summary = df.groupby(["period","sentiment"]).size().unstack(fill_value=0)
props   = summary.div(summary.sum(axis=1), axis=0)
print("\nSentiment counts by period:\n", summary)
print("\nSentiment proportions by period:\n", props)
