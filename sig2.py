import csv
import time
import pyautogui
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
#options.add_argument("--headless")  # Uncomment for headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Read Swiggy swiggys from CSV
review = pd.read_csv("categories.csv")

# Ensure 'swiggy' column exists and filter valid URLs
if 'swiggy' not in review.columns:
    print("❌ 'swiggy' column not found in CSV!")
    driver.quit()
    exit()

valid_urls = review[pd.notna(review['swiggy']) & review['swiggy'].str.startswith('http', na=False)]
print(f"✅ {len(valid_urls)} valid URLs found")

# CSV File Setup
csv_filename = "swiggy_products.csv"

with open(csv_filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Name", "Price", "Weight", "URL"])


    # Process each URL
    for i, row in valid_urls.iterrows():
        
        url = row['swiggy']

        try:
            driver.get(url)

            # ✅ Wait until products load
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="ItemWidgetContainer"]'))
            )

            # ✅ Dynamic Scrolling to load all products
            scroll_attempts, max_stagnant_attempts = 0, 3
            stagnant_attempts = 0
            previous_product_count = 0

            time.sleep(2)  # Allow initial elements to render
            while stagnant_attempts < max_stagnant_attempts:
                pyautogui.scroll(-10000)  # Scroll down
                time.sleep(3)  # Allow new elements to load

                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                products = soup.select('div[data-testid="ItemWidgetContainer"]')
                current_product_count = len(products)

                if current_product_count == previous_product_count:
                    stagnant_attempts += 1
                else:
                    stagnant_attempts = 0

                previous_product_count = current_product_count

            time.sleep(3)  # Ensure all elements are loaded
            soup = BeautifulSoup(driver.page_source, "html.parser")
            products = soup.select('div[data-testid="ItemWidgetContainer"]')

            # ✅ Retry extraction if too few products found
            if len(products) < 5:
                print("⚠️ Too few products found, retrying extraction...")
                time.sleep(5)
                soup = BeautifulSoup(driver.page_source, "html.parser")
                products = soup.select('div[data-testid="ItemWidgetContainer"]')

            print(f"✅ {len(products)} products found on {url}")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for product in products:
                try:
                    name = product.select_one("div.novMV").text.strip()
                    price = product.select_one("div[data-testid='itemOfferPrice']").text.strip()
                    
                    # ✅ Extract weight from aria-label
                    try:
                        weight = product.select_one("div[aria-label]").get("aria-label").strip()
                    except:
                        weight = "N/A"  # Default if weight is missing
                    
                    writer.writerow([timestamp, name, price, weight, url])
                    print(f"Product: {name} | Price: {price} | Weight: {weight}")
                    print("-" * 40)
                except Exception as e:
                    print("❌ Error extracting product details:", e)


        except Exception as e:
            print(f"❌ Error loading URL ({url}):", e)

# ✅ Close Selenium
driver.quit()
print(f"✅ Data appended to {csv_filename}")
