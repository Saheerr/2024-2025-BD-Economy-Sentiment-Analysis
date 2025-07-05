
import pandas as pd


df = pd.read_csv("bangladesh_headlines.csv")


local_keywords = [
    'bangladesh', 'bdt', 'taka', 'dhaka', 'remittance', 'import', 'export',
    'padma', 'nagad', 'budget', 'inflation', 'garment', 'rmg', 'loan', 'reserve',
    'foreign aid', 'world bank', 'adb', 'imf', 'policy', 'bonds', 'currency'
]


def flag_relevance(title):
    title_lower = title.lower()
    for keyword in local_keywords:
        if keyword in title_lower:
            return "likely relevant"
    return "possibly irrelevant"

df["relevance_flag"] = df["title"].apply(flag_relevance)


df = df.drop_duplicates(subset="title", keep="first")


df.to_csv("bangladesh_headlines_with_urls_flagged.csv", index=False)
print(f"✅ Done! Flagged {len(df)} headlines based on relevance.")
