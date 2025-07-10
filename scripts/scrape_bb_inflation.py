#!/usr/bin/env python3
import os
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

df = pd.read_csv("data/bb_inflation_monthly_2023_2025.csv", parse_dates=["date"])
june2025 = pd.to_datetime("2025-06-01")
df.loc[df["date"] == june2025, "ptp_inflation_pct"] = 8.48
df.to_csv("data/bb_inflation_monthly_2023_2025.csv", index=False)

print("🔧 June 2025 rate overridden in place")

driver_path = "./chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


url = "https://www.bb.org.bd/en/index.php/econdata/inflation"
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "slctyear")))
wait.until(EC.presence_of_element_located((By.NAME, "slctmonth")))


dates = pd.date_range("2023-01-01", "2025-07-01", freq="MS")
records = []

for dt in dates:
    year = str(dt.year)
    month = dt.strftime("%B")
    date_str = dt.strftime("%Y-%m-01")

   
    Select(driver.find_element(By.NAME, "slctyear")).select_by_visible_text(year)
    Select(driver.find_element(By.NAME, "slctmonth")).select_by_visible_text(month)

    
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    wait.until(EC.presence_of_element_located((By.ID, "sortableTable")))
    time.sleep(0.2)

    
    rows = driver.find_elements(By.CSS_SELECTOR, "#sortableTable tbody tr")
    ptp = ma12 = None

    for tr in rows:
        cols = tr.find_elements(By.TAG_NAME, "td")
        if len(cols) < 2:
            continue
        label = cols[0].text.lower()
        try:
            val = float(cols[1].text.replace("%", "").strip())
        except ValueError:
            continue

        if "point to point" in label:
            ptp = val
        elif "monthly average" in label:
            ma12 = val

    if ptp is not None and ma12 is not None:
        records.append({
            "date": date_str,
            "ptp_inflation_pct": ptp,
            "ma12_inflation_pct": ma12
        })
    else:
        print(f"⚠️  missing data for {date_str}: ptp={ptp}, ma12={ma12}")

driver.quit()


df = pd.DataFrame(records)
os.makedirs("data", exist_ok=True)
out_path = "data/bb_inflation_monthly_2023_2025.csv"
df.to_csv(out_path, index=False)
print(f"✅  Saved {len(df)} rows to {out_path}")
