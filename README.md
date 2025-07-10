#  Bangladesh Economic Sentiment & Inflation Analysis (2023–2025)

This project analyzes the economic sentiment in Bangladesh during the transition from the Hasina regime to the 2024–2025 interim government. Although the Hasina regime started from 2009 and ended on August 2024, I am only taking in data from 2023-2025. The study uses **news sentiment analysis** and **macroeconomic indicators** (inflation and GDP) to evaluate how economic perception and reality shifted across the transition. Headlines from *The Daily Star* (via Google News RSS) are analyzed using **VADER sentiment analysis**, and compared with inflation and GDP data from the **Bangladesh Bank** and the **IMF World Economic Outlook**.

---

##  Project Goal

> To compare public economic sentiment and real economic indicators during Sheikh Hasina's final years in power vs. the interim government, and assess whether public perception aligns with macroeconomic performance.

---

##  Data Sources

| Source                  | Dataset                                  | Description |
|------------------------|-------------------------------------------|-------------|
| Google News RSS        | Economic Headlines                        | Filtered by date and keyword for Bangladesh economy |
| IMF World Economic Outlook | GDP & Inflation Forecasts           | Annual data for 2023–2025 |
| Bangladesh Bank (scraped) | Monthly CPI YoY Inflation | Official inflation figures scraped from BB’s website, originally based on BBS data |
| Business Standard (7 July 2025)     | June 2025 Inflation Summary      | *"Inflation in Bangladesh has dropped below 9% for the first time in 27 months.

---

##  Data Note: June 2025 Inflation 

According to new data released by the **Bangladesh Bureau of Statistics (BBS)** on **7 July 2025** (as reported by *The Business Standard*), Bangladesh’s **point-to-point inflation rate** fell below 9% for the first time in 27 months:

- **June 2025**: 8.48%  
- **May 2025**: 9.05%  
- **Highest inflation during the period**: 11.66% in **July 2024**

Further breakdown:
- **Food inflation**: 7.39% in June (down from 8.59% in May)
- **Non-food inflation**: 9.37% in June (down slightly from 9.42% in May)

This context supports our analysis of **sentiment improvements in mid-2025**, aligning with easing inflationary pressure during the post-transition period.

> 📎 *Source: “Inflation drops below 9% after 27 months,” The Business Standard (7 July 2025)*  
> *Data originally published by the Bangladesh Bureau of Statistics (BBS).*

---

##  Tools and Libraries

###  Web Scraping & Automation
- **Selenium** – Automated inflation data scraping from the Bangladesh Bank website using a headless Chrome browser.
- **feedparser** – Parsed economic headlines from Google News RSS feeds.
- **urllib.parse** – Encoded dynamic query strings for Google News RSS URL construction.

###  Data Manipulation
- **pandas** – Core library for loading, cleaning, transforming, and merging CSV datasets.
- **numpy** – Used for numerical computations and constructing grouped bar plots.

###  Sentiment Analysis
- **vaderSentiment** – Rule-based sentiment analysis library used to classify headlines as Positive, Negative, or Neutral based on compound scores.

###  Date & Time Handling
- **datetime**, **timedelta**, **pandas.date_range** – Managed monthly windows, time filtering, and period labeling for macro and sentiment data.

###  Visualization
- **matplotlib.pyplot** – Primary plotting library used to create static charts comparing sentiment, inflation, and GDP growth.

---

##  Methodology

### 1. Headline Collection
- Collected RSS headlines using date windows from Jan 2023 to July 2025.
- Duplicate URLs removed to avoid double-counting.

### 2. Sentiment Classification
- Used **VADER sentiment analyzer** to score each headline.
- Classified headlines as:
  - **Positive** (compound ≥ 0.05)
  - **Negative** (compound ≤ –0.05)
  - **Neutral** (otherwise)

---

## Visualizations

### Annual Inflation (Actual & Forecast)

### GDP Growth vs. Inflation (2023–2025)

### Monthly Point-to-Point Inflation (Jan 2023 – Jul 2025)

### News Sentiment Counts by Period (Jan 2023 – Jul 2025)

### News Sentiment Proportions by Period (Jan 2023 – Jul 2025)

### Bangladesh (2023–2025): Forecasts vs Sentiment

---

## Limitations

- English-only headlines (via Google News RSS) may not fully capture grassroots perception.
- IMF data is annual, limiting monthly comparison resolution.
- Headline sentiment is not equals to general population sentiment.

---


## Author

**Saheer Rahman**  
Computer Science @ University at Buffalo  
Economics Minor  
> Portfolio: [saheerportfolio.vercel.app](https://saheerportfolio.vercel.app/)  
> GitHub: [@Saheerr](https://github.com/Saheerr)

---

##  License

Open-source project. Feel free to use for academic or journalistic purposes with attribution.

---
