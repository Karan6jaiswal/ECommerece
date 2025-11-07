from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re, time

# ---------- CONFIG ----------
input_csv = "zepto_fruits.csv"
output_csv = "zepto_fruits_enriched.csv"

options = Options()
# options.add_argument("--headless=new")  # uncomment for silent run
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

def safe_get(css, attr=None):
    try:
        el = driver.find_element(By.CSS_SELECTOR, css)
        return el.text.strip() if not attr else el.get_attribute(attr)
    except NoSuchElementException:
        return ""

def extract_rupee_num(s):
    m = re.search(r'₹\s*([0-9]+(?:\.[0-9]+)?)', s)
    return m.group(1) if m else ""

def get_discount_text():
    try:
        el = driver.find_element(By.XPATH, '//*[contains(normalize-space(.), "OFF")]')
        return el.text.strip()
    except NoSuchElementException:
        return ""

def scrape_product_page(url):
    driver.get(url)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-slot-id="ProductName"]')))
    except TimeoutException:
        return None  # skip if page fails to load

    name = safe_get('[data-slot-id="ProductName"]')
    pack = safe_get('[data-slot-id="PackSize"]')
    price = safe_get('[data-slot-id="EdlpPrice"]') or safe_get('[data-slot-id="Price"]')
    mrp = safe_get('[data-slot-id="CompareAtPrice"]')
    discount = get_discount_text()
    img = safe_get('[data-slot-id="ProductImageWrapper"] img', "src")
    oos = "true" if driver.find_elements(By.CSS_SELECTOR, '[data-is-out-of-stock="true"]') else "false"

    return {
        "name": name,
        "pack_size": pack,
        "price_rs": extract_rupee_num(price),
        "mrp_rs": extract_rupee_num(mrp),
        "discount_text": discount,
        "out_of_stock": oos,
        "img_url": img,
        "raw_price_block": (price + " " + mrp).strip()
    }

# ---------- LOAD EXISTING DATA ----------
df = pd.read_csv(input_csv)

# Identify rows with missing name but valid product_url
missing_rows = df[df['name'].isna() | (df['name'].astype(str).str.strip() == "")]
missing_rows = missing_rows[missing_rows['product_url'].notna()]

print(f"Found {len(missing_rows)} incomplete products to update...")

# ---------- SCRAPE EACH ----------
updated_data = []
for i, row in missing_rows.iterrows():
    url = row['product_url']
    print(f"Scraping {i+1}/{len(missing_rows)} → {url}")
    data = scrape_product_page(url)
    if data:
        for k, v in data.items():
            df.at[i, k] = v
    else:
        print(f"⚠️ Skipped (load error): {url}")
    time.sleep(2)

driver.quit()

# ---------- SAVE UPDATED FILE ----------
df.to_csv(output_csv, index=False)
print(f"\n✅ Enriched CSV saved as {output_csv}")
