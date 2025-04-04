# # import csv
# # import pandas as pd
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from bs4 import BeautifulSoup
# # import time
# # from webdriver_manager.chrome import ChromeDriverManager

# # # Setup Selenium WebDriver
# # options = Options()
# # options.add_argument("--disable-blink-features=AutomationControlled")
# # options.add_argument("--start-maximized")
# # options.add_argument("--disable-gpu")
# # # options.add_argument("--headless")  # Uncomment to run in headless mode

# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # Open JioMart URL
# # review=pd.read_csv(r"C:\Users\admin\Desktop\Python\categories.csv")
# # print(len(review))
# # for i in range(1,len(review)):
    
    
# #     url = review['jiomart'][i]
# #     driver.get(url)

# #     # ✅ Wait until products load (15 sec max)
# #     try:
# #         WebDriverWait(driver, 5).until(
# #             EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ais-InfiniteHits-list li.ais-InfiniteHits-item"))
# #         )
# #     except Exception as e:
# #         print("❌ Page did not load properly:", e)
# #         driver.quit()
# #         exit()

# #     # Scroll multiple times to load all products
# #     for _ in range(10):
# #         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
# #         time.sleep(1)

# #     # Get page source for BeautifulSoup
# #     html = driver.page_source
# #      # ✅ Close Selenium

# #     # Parse with BeautifulSoup
# #     soup = BeautifulSoup(html, "html.parser")

# #     # Extract product details
# #     products = soup.select("ol.ais-InfiniteHits-list li.ais-InfiniteHits-item")
# #     print(f"✅ Found {len(products)} products")

# #     # CSV File Setup
# #     csv_filename = "jiomart_products.csv"
# #     with open(csv_filename, "w", newline="", encoding="utf-8") as file:
# #         writer = csv.writer(file)
# #         writer.writerow(["Name", "Price", "URL"])  # CSV Headers

# #         for product in products:
# #             try:
# #                 name = product.select_one("div.plp-card-details-name").text.strip()
# #                 price = product.select_one("div.plp-card-details-price span").text.strip()
# #                 image_url = product.select_one("div.plp-card-image img")["src"]

# #                 # Write to CSV
# #                 writer.writerow([name, price, image_url])

# #                 # Print Output
# #                 print(f"Product: {name}")
# #                 print(f"Price: {price}")
# #                 print(f"Image: {image_url}")
# #                 print("-" * 40)

# #             except Exception as e:
# #                 print("❌ Error extracting product details:", e)
# #     print(i)
# # driver.quit() 
# # print(f"✅ Data saved to {csv_filename}")
# import csv
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time
# from webdriver_manager.chrome import ChromeDriverManager

# # Setup Selenium WebDriver
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-gpu")
# # options.add_argument("--headless")  # Uncomment for headless mode

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Read CSV File
# review = pd.read_csv(r"C:\Users\admin\Desktop\Python\categories.csv")

# # Ensure 'jiomart' column exists
# if 'jiomart' not in review.columns:
#     print("❌ 'jiomart' column not found in CSV!")
#     driver.quit()
#     exit()

# # Filter valid URLs
# valid_urls = review[pd.notna(review['jiomart']) & review['jiomart'].str.startswith('http', na=False)]

# print(f"✅ {len(valid_urls)} valid URLs found")

# # CSV File Setup
# csv_filename = "jiomart_products.csv"
# with open(csv_filename, "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Price", "URL"])  # CSV Headers

#     # Process each URL
#     for i, row in valid_urls.iterrows():
#         url = row['jiomart']

#         # ✅ Skip invalid URLs
#         if not isinstance(url, str) or not url.startswith("http"):
#             print(f"⚠️ Skipping invalid URL at index {i}: {url}")
#             continue

#         print(f"🔗 Processing: {url}")

#         try:
#             driver.get(url)

#             # ✅ Wait until products load
#             try:
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ais-InfiniteHits-list li.ais-InfiniteHits-item"))
#                 )
#             except Exception as e:
#                 print(f"⚠️ Page did not load properly for {url}: {e}")
#                 continue  # Skip to the next URL

#             # Scroll multiple times to load all products
#             for _ in range(10):
#                 driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#                 time.sleep(1)

#             # Get page source for BeautifulSoup
#             html = driver.page_source
#             soup = BeautifulSoup(html, "html.parser")

#             # Extract product details
#             products = soup.select("ol.ais-InfiniteHits-list li.ais-InfiniteHits-item")
#             print(f"✅ Found {len(products)} products")

#             for product in products:
#                 try:
#                     name = product.select_one("div.plp-card-details-name")
#                     name = name.text.strip() if name else "N/A"

#                     price = product.select_one("div.plp-card-details-price span")
#                     price = price.text.strip() if price else "N/A"

#                     image_url = product.select_one("div.plp-card-image img")
#                     image_url = image_url["src"] if image_url else "N/A"

#                     # Write to CSV
#                     writer.writerow([name, price, image_url])

#                     # Print Output
#                     print(f"🛍️ Product: {name}")
#                     print(f"💰 Price: {price}")
#                     print(f"🖼️ Image: {image_url}")
#                     print("-" * 40)

#                 except Exception as e:
#                     print("❌ Error extracting product details:", e)

#         except Exception as e:
#             print(f"❌ Error loading URL ({url}):", e)

# # ✅ Close Selenium
# driver.quit()
# print(f"✅ Data saved to {csv_filename}")
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium WebDriver
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
# options.add_argument("--headless")  # Uncomment for headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Read CSV File
review = pd.read_csv(r"C:\Users\admin\Desktop\Python\categories.csv")

# Ensure 'jiomart' column exists
if 'jiomart' not in review.columns:
    print("❌ 'jiomart' column not found in CSV!")
    driver.quit()
    exit()

# Filter valid URLs
valid_urls = review[pd.notna(review['jiomart']) & review['jiomart'].str.startswith('http', na=False)]

print(f"✅ {len(valid_urls)} valid URLs found")

# CSV File Setup
csv_filename = "jiomart_products.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Weight", "URL", "Timestamp"])  # CSV Headers

    # Process each URL
    for i, row in valid_urls.iterrows():
        url = row['jiomart']

        # ✅ Skip invalid URLs
        if not isinstance(url, str) or not url.startswith("http"):
            print(f"⚠️ Skipping invalid URL at index {i}: {url}")
            continue

        print(f"🔗 Processing: {url}")

        try:
            driver.get(url)

            # ✅ Wait until products load
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ais-InfiniteHits-list li.ais-InfiniteHits-item"))
                )
            except Exception as e:
                print(f"⚠️ Page did not load properly for {url}: {e}")
                continue  # Skip to the next URL

            # Scroll multiple times to load all products
            for _ in range(10):
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
                time.sleep(1)

            # Get page source for BeautifulSoup
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            # Extract product details
            products = soup.select("ol.ais-InfiniteHits-list li.ais-InfiniteHits-item")
            print(f"✅ Found {len(products)} products")

            for product in products:
                try:
                    name = product.select_one("div.plp-card-details-name")
                    name = name.text.strip() if name else "N/A"

                    price = product.select_one("div.plp-card-details-price span")
                    price = price.text.strip() if price else "N/A"

                    weight = product.select_one("span.variant_value")
                    weight = weight.text.strip() if weight else "N/A"

                    image_url = product.select_one("div.plp-card-image img")
                    image_url = image_url["src"] if image_url else "N/A"

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Write to CSV
                    writer.writerow([name, price, weight, image_url, timestamp])

                    # Print Output
                    print(f"🛍️ Product: {name}")
                    print(f"💰 Price: {price}")
                    print(f"⚖️ Weight: {weight}")
                    print(f"🖼️ Image: {image_url}")
                    print(f"⏰ Timestamp: {timestamp}")
                    print("-" * 40)

                except Exception as e:
                    print("❌ Error extracting product details:", e)

        except Exception as e:
            print(f"❌ Error loading URL ({url}):", e)

# ✅ Close Selenium
driver.quit()
print(f"✅ Data saved to {csv_filename}")
