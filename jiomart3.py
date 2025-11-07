from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# -----------------------
# CONFIGURATION
# -----------------------
URL = "https://www.jiomart.com/c/groceries/cooking-essentials/atta-flours-sooji/28985"
CSV_FILE = "jiomart_atta_products_full.csv"
SCROLL_PAUSE_TIME = 2  # seconds
PAGE_WAIT_LIMIT = 10   # seconds if no change in height

# -----------------------
# SELENIUM SETUP
# -----------------------
options = Options()
#options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=options)
driver.get(URL)

# -----------------------
# SCROLL TO LOAD ALL PRODUCTS
# -----------------------
last_height = driver.execute_script("return document.body.scrollHeight")
start_wait_time = time.time()

print("📜 Scrolling to load all products...")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        if time.time() - start_wait_time > PAGE_WAIT_LIMIT:
            print("⚠️ Page stopped loading for 10 seconds. Finishing scroll...")
            break
    else:
        start_wait_time = time.time()  # Reset timer when new content loads

    last_height = new_height

# Wait for all products to be visible
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ais-InfiniteHits-item"))
)

# -----------------------
# PARSE HTML USING BEAUTIFULSOUP
# -----------------------
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

products = soup.find_all("li", class_="ais-InfiniteHits-item")
print(f"✅ Total products found: {len(products)}")

data = []

# -----------------------
# SCRAPE AND PRINT PRODUCT DETAILS
# -----------------------
for idx, product in enumerate(products, start=1):
    try:
        name = product.find("div", class_="plp-card-details-name").get_text(strip=True)
    except:
        name = None

    try:
        price = product.find("span", class_="jm-heading-xxs jm-mb-xxs").get_text(strip=True)
    except:
        price = None

    try:
        old_price = product.find("span", class_="jm-body-xxs jm-fc-primary-grey-60 line-through").get_text(strip=True)
    except:
        old_price = None

    try:
        discount = product.find("span", class_="jm-badge").get_text(strip=True)
    except:
        discount = None

    try:
        weight = product.find("span", class_="jm-body-s-bold jm-fc-primary-60 variant_value").get_text(strip=True)
    except:
        weight = None

    try:
        link = "https://www.jiomart.com" + product.find("a")["href"]
    except:
        link = None

    product_info = {
        "Product Name": name,
        "Price": price,
        "Old Price": old_price,
        "Discount": discount,
        "Weight": weight,
        "Product Link": link
    }

    data.append(product_info)

    # Print as scraping proceeds
    print(f"{idx}. {name} | {price} | {discount} | {weight}")

# -----------------------
# SAVE TO CSV
# -----------------------
df = pd.DataFrame(data)
df.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")

print("\n🎯 Scraping completed successfully!")
print(f"💾 Data saved to: {CSV_FILE}")
