

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.thedailystar.net/business/economy"
driver.get(url)
time.sleep(3)


SCROLL_PAUSE = 2
last_height = driver.execute_script("return document.body.scrollHeight")
headlines = set()

while True:
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE)

    
    articles = driver.find_elements(By.CSS_SELECTOR, "h3.title a")
    for a in articles:
        title = a.text.strip()
        link = a.get_attribute("href")
        if title and link and "/business/economy" in link:
            headlines.add((title, link))

    
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

driver.quit()


df = pd.DataFrame(headlines, columns=["title", "url"])
df.to_csv("bangladesh_headlines.csv", index=False)
print(f"✅ Done! Scraped {len(df)} unique headlines.")
