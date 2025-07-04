from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

headlines = []


local_keywords = ['bangladesh', 'taka', 'bdt', 'dhaka', 'remittance', 'export', 'import', 'garment', 'padma', 'budget', 'nagad']


for page in range(1, 21):
    url = f"https://www.thedailystar.net/business/economy?page={page}"
    print(f"Scraping page {page}...")
    driver.get(url)
    time.sleep(6)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all('a', href=True):
        title = tag.text.strip()
        href = tag['href']

        if title and len(title.split()) >= 3 and "/business/economy" in href:
            full_url = "https://www.thedailystar.net" + href

          
            is_local = any(word in title.lower() for word in local_keywords)
            relevance_flag = "likely relevant" if is_local else "possibly irrelevant"

            headlines.append({'title': title, 'url': full_url, 'relevance_flag': relevance_flag})

driver.quit()

df = pd.DataFrame(headlines).drop_duplicates(subset='title', keep='first')


df.to_csv("bangladesh_headlines_with_urls_flagged.csv", index=False)
print(f"✅ Done! Scraped {len(df)} unique headlines with URLs and relevance flags.")
