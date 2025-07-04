from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

headlines = []


for page in range(1, 21):
    url = f"https://www.thedailystar.net/business/economy?page={page}"
    print(f"Scraping page {page}...")
    driver.get(url)
    time.sleep(6)  
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all(['h1', 'h2', 'h3']):
        title = tag.text.strip()
        if title and len(title.split()) > 4:  
            headlines.append({'title': title})

driver.quit()


df = pd.DataFrame(headlines)
df.to_csv("bangladesh_headlines.csv", index=False)
print(f"✅ Done! Scraped {len(df)} headlines.")
