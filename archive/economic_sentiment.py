from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


df = pd.read_csv("bangladesh_headlines.csv")


analyzer = SentimentIntensityAnalyzer()

l
def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'


df['sentiment'] = df['title'].apply(get_sentiment)


df.to_csv("headlines_with_sentiment.csv", index=False)
print("✅ Sentiment analysis complete. Saved to 'headlines_with_sentiment.csv'.")
