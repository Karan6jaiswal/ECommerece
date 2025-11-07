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
# # review=pd.read_csv(r"C:\Users\admin\Desktop\Python\jiomart_all_links.csv")
# # print(len(review))
# # for i in range(1,len(review)):
    
    
# #     url = review['URL'][i]
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
# # # import csv
# # # import pandas as pd
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from bs4 import BeautifulSoup
# # # import time
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # Setup Selenium WebDriver
# # # options = Options()
# # # options.add_argument("--disable-blink-features=AutomationControlled")
# # # options.add_argument("--start-maximized")
# # # options.add_argument("--disable-gpu")
# # # # options.add_argument("--headless")  # Uncomment for headless mode

# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # Read CSV File
# # # review = pd.read_csv(r"C:\Users\admin\Desktop\Python\categories.csv")

# # # # Ensure 'jiomart' column exists
# # # if 'jiomart' not in review.columns:
# # #     print("❌ 'jiomart' column not found in CSV!")
# # #     driver.quit()
# # #     exit()

# # # # Filter valid URLs
# # # valid_urls = review[pd.notna(review['jiomart']) & review['jiomart'].str.startswith('http', na=False)]

# # # print(f"✅ {len(valid_urls)} valid URLs found")

# # # # CSV File Setup
# # # csv_filename = "jiomart_products.csv"
# # # with open(csv_filename, "w", newline="", encoding="utf-8") as file:
# # #     writer = csv.writer(file)
# # #     writer.writerow(["Name", "Price", "URL"])  # CSV Headers

# # #     # Process each URL
# # #     for i, row in valid_urls.iterrows():
# # #         url = row['jiomart']

# # #         # ✅ Skip invalid URLs
# # #         if not isinstance(url, str) or not url.startswith("http"):
# # #             print(f"⚠️ Skipping invalid URL at index {i}: {url}")
# # #             continue

# # #         print(f"🔗 Processing: {url}")

# # #         try:
# # #             driver.get(url)

# # #             # ✅ Wait until products load
# # #             try:
# # #                 WebDriverWait(driver, 10).until(
# # #                     EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ais-InfiniteHits-list li.ais-InfiniteHits-item"))
# # #                 )
# # #             except Exception as e:
# # #                 print(f"⚠️ Page did not load properly for {url}: {e}")
# # #                 continue  # Skip to the next URL

# # #             # Scroll multiple times to load all products
# # #             for _ in range(10):
# # #                 driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
# # #                 time.sleep(1)

# # #             # Get page source for BeautifulSoup
# # #             html = driver.page_source
# # #             soup = BeautifulSoup(html, "html.parser")

# # #             # Extract product details
# # #             products = soup.select("ol.ais-InfiniteHits-list li.ais-InfiniteHits-item")
# # #             print(f"✅ Found {len(products)} products")

# # #             for product in products:
# # #                 try:
# # #                     name = product.select_one("div.plp-card-details-name")
# # #                     name = name.text.strip() if name else "N/A"

# # #                     price = product.select_one("div.plp-card-details-price span")
# # #                     price = price.text.strip() if price else "N/A"

# # #                     image_url = product.select_one("div.plp-card-image img")
# # #                     image_url = image_url["src"] if image_url else "N/A"

# # #                     # Write to CSV
# # #                     writer.writerow([name, price, image_url])

# # #                     # Print Output
# # #                     print(f"🛍️ Product: {name}")
# # #                     print(f"💰 Price: {price}")
# # #                     print(f"🖼️ Image: {image_url}")
# # #                     print("-" * 40)

# # #                 except Exception as e:
# # #                     print("❌ Error extracting product details:", e)

# # #         except Exception as e:
# # #             print(f"❌ Error loading URL ({url}):", e)

# # # # ✅ Close Selenium
# # # driver.quit()
# # # print(f"✅ Data saved to {csv_filename}")
# # # ------
# # # import csv
# # # import pandas as pd
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from bs4 import BeautifulSoup
# # # import time
# # # from datetime import datetime
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # Setup Selenium WebDriver
# # # options = Options()
# # # options.add_argument("--disable-blink-features=AutomationControlled")
# # # options.add_argument("--start-maximized")
# # # options.add_argument("--disable-gpu")
# # # options.add_argument("--headless")  # Uncomment for headless mode

# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # Read CSV File
# # # review = pd.read_csv("categories.csv")

# # # # Ensure 'jiomart' column exists
# # # if 'jiomart' not in review.columns:
# # #     print("❌ 'jiomart' column not found in CSV!")
# # #     driver.quit()
# # #     exit()

# # # # Filter valid URLs
# # # valid_urls = review[pd.notna(review['jiomart']) & review['jiomart'].str.startswith('http', na=False)]

# # # print(f"✅ {len(valid_urls)} valid URLs found")

# # # # CSV File Setup
# # # csv_filename = "jiomart_products.csv"
# # # with open(csv_filename, "a", newline="", encoding="utf-8") as file:
# # #     writer = csv.writer(file)
# # #     writer.writerow(["Name", "Price", "Weight", "URL", "Timestamp"])  # CSV Headers

# # #     # Process each URL
# # #     for i, row in valid_urls.iterrows():
# # #         url = row['jiomart']

# # #         # ✅ Skip invalid URLs
# # #         if not isinstance(url, str) or not url.startswith("http"):
# # #             print(f"⚠️ Skipping invalid URL at index {i}: {url}")
# # #             continue

# # #         print(f"🔗 Processing: {url}")

# # #         try:
# # #             driver.get(url)

# # #             # ✅ Wait until products load
# # #             try:
# # #                 WebDriverWait(driver, 10).until(
# # #                     EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ais-InfiniteHits-list li.ais-InfiniteHits-item"))
# # #                 )
# # #             except Exception as e:
# # #                 print(f"⚠️ Page did not load properly for {url}: {e}")
# # #                 continue  # Skip to the next URL

# # #             # Scroll multiple times to load all products
# # #             for _ in range(10):
# # #                 driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
# # #                 time.sleep(1)

# # #             # Get page source for BeautifulSoup
# # #             html = driver.page_source
# # #             soup = BeautifulSoup(html, "html.parser")

# # #             # Extract product details
# # #             products = soup.select("ol.ais-InfiniteHits-list li.ais-InfiniteHits-item")
# # #             print(f"✅ Found {len(products)} products")

# # #             for product in products:
# # #                 try:
# # #                     name = product.select_one("div.plp-card-details-name")
# # #                     name = name.text.strip() if name else "N/A"

# # #                     price = product.select_one("div.plp-card-details-price span")
# # #                     price = price.text.strip() if price else "N/A"

# # #                     weight = product.select_one("span.variant_value")
# # #                     weight = weight.text.strip() if weight else "N/A"

# # #                     image_url = product.select_one("div.plp-card-image img")
# # #                     image_url = image_url["src"] if image_url else "N/A"

# # #                     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # #                     # Write to CSV
# # #                     writer.writerow([name, price, weight, image_url, timestamp])

# # #                     # Print Output
# # #                     print(f"🛍️ Product: {name}")
# # #                     print(f"💰 Price: {price}")
# # #                     print(f"⚖️ Weight: {weight}")
# # #                     print(f"🖼️ Image: {image_url}")
# # #                     print(f"⏰ Timestamp: {timestamp}")
# # #                     print("-" * 40)

# # #                 except Exception as e:
# # #                     print("❌ Error extracting product details:", e)

# # #         except Exception as e:
# # #             print(f"❌ Error loading URL ({url}):", e)

# # # # ✅ Close Selenium
# # # driver.quit()

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
# from datetime import datetime
# from webdriver_manager.chrome import ChromeDriverManager

# # ======================
# # Setup Selenium WebDriver
# # ======================
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-gpu")
# # options.add_argument("--headless")  # Uncomment for headless mode if needed

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # ======================
# # Read CSV File
# # ======================
# review = pd.read_csv("jiomart_all_links.csv")

# if 'URL' not in review.columns:
#     print("❌ 'jiomart' column not found in CSV!")
#     driver.quit()
#     exit()

# valid_urls = review[pd.notna(review['URL']) & review['URL'].str.startswith('http', na=False)]
# print(f"✅ {len(valid_urls)} valid URLs found")

# # ======================
# # CSV File Setup
# # ======================
# csv_filename = "jiomart_products.csv"
# with open(csv_filename, "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Price", "Weight", "Image_URL", "URL", "Timestamp"])  # CSV Headers

#     # ======================
#     # Process each URL
#     # ======================
#     for i, row in valid_urls.iterrows():
#         url = row['URL']

#         if not isinstance(url, str) or not url.startswith("http"):
#             print(f"⚠️ Skipping invalid URL at index {i}: {url}")
#             continue

#         print(f"🔗 Processing: {url}")

#         try:
#             driver.get(url)

#             # ✅ Wait for product cards to load
#             WebDriverWait(driver, 15).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.plp-card"))
#             )

#             # ✅ Scroll until no new products load
#             last_height = driver.execute_script("return document.body.scrollHeight")
#             while True:
#                 driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#                 time.sleep(2)
#                 new_height = driver.execute_script("return document.body.scrollHeight")
#                 if new_height == last_height:
#                     break
#                 last_height = new_height

#             # ✅ Get page source
#             soup = BeautifulSoup(driver.page_source, "html.parser")
#             products = soup.select("div.plp-card")
#             print(f"✅ Found {len(products)} products")

#             for product in products:
#                 try:
#                     name = product.select_one("div.plp-card-details-name")
#                     name = name.text.strip() if name else "N/A"

#                     price = product.select_one("span.jm-heading-xxs")
#                     price = price.text.strip() if price else "N/A"

#                     weight = product.select_one("span.jm-body-xs")
#                     weight = weight.text.strip() if weight else "N/A"

#                     image_url = product.select_one("img")
#                     image_url = image_url["src"] if image_url else "N/A"

#                     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#                     writer.writerow([name, price, weight, image_url, url, timestamp])

#                     print(f"🛍️ {name}")
#                     print(f"💰 {price}")
#                     print(f"⚖️ {weight}")
#                     print(f"🖼️ {image_url}")
#                     print(f"⏰ {timestamp}")
#                     print("-" * 40)

#                 except Exception as e:
#                     print("❌ Error extracting product details:", e)

#         except Exception as e:
#             print(f"❌ Error loading URL ({url}): {e}")

# # ✅ Close Selenium
# driver.quit()
# print(f"✅ Data saved to {csv_filename}")

# # print(f"✅ Data saved to {csv_filename}")








# pip install selenium webdriver-manager pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re
import time

# ---------- Helpers ----------

QUANTITY_RE = re.compile(r'(\d+(?:\.\d+)?)\s*(kg|g|gm|ml|l|L|pcs|pc|pack|packs|piece|pieces|cm|m)\b', re.I)

def extract_quantity(texts):
    """Try to pull a quantity/weight from several candidate strings."""
    for t in filter(None, texts):
        m = QUANTITY_RE.search(t)
        if m:
            num, unit = m.groups()
            unit = unit.lower().replace('gm', 'g').replace('pc', 'pcs')
            return f"{num} {unit}"
    return ""

def first_nonempty(*vals):
    for v in vals:
        if v:
            return v
    return ""

def get_text_safe(el, css):
    try:
        return el.find_element(By.CSS_SELECTOR, css).text.strip()
    except:
        return ""

def get_attr_safe(el, css, attr):
    try:
        return el.find_element(By.CSS_SELECTOR, css).get_attribute(attr) or ""
    except:
        return ""

# ---------- Core scraper ----------

def scrape_category(url, max_scroll_pause=0.8, max_idle_rounds=6, headless=True):
    opts = webdriver.ChromeOptions()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--window-size=1400,1200")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--log-level=3")
    opts.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    wait = WebDriverWait(driver, 20)

    try:
        driver.get(url)

        # Wait for any product list to appear
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "ol.ais-InfiniteHits-list, li.ais-InfiniteHits-item")
            )
        )

        # Infinite scroll until product count stops increasing for a few rounds
        last_count, idle_rounds = 0, 0
        while True:
            # Scroll to bottom to trigger fetch
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(max_scroll_pause)

            # Sometimes Jiomart loads in chunks—poke it a bit
            driver.execute_script("window.scrollBy(0, -300);")
            time.sleep(0.25)
            driver.execute_script("window.scrollBy(0, 600);")

            cards = driver.find_elements(By.CSS_SELECTOR, "li.ais-InfiniteHits-item")
            count = len(cards)
            if count <= last_count:
                idle_rounds += 1
            else:
                idle_rounds = 0
                last_count = count

            if idle_rounds >= max_idle_rounds:
                break

        # Parse product cards
        data = []
        cards = driver.find_elements(By.CSS_SELECTOR, "li.ais-InfiniteHits-item")
        for li in cards:
            try:
                root_a = li.find_element(By.CSS_SELECTOR, "a.plp-card-wrapper")
            except:
                # Some list items are placeholders
                continue

            # --- name ---
            name = get_text_safe(li, "div.plp-card-details-name")

            # --- price (current) & MRP (struck-through) ---
            price_raw = first_nonempty(
                get_text_safe(li, "div.plp-card-details-price span.jm-heading-xxs"),
                get_text_safe(li, "div.plp-card-details-price-wrapper span.jm-heading-xxs"),
            )
            # strip currency and commas to numeric if you want; here keep the text
            mrp_raw = get_text_safe(li, "div.plp-card-details-price span.line-through")

            # --- discount badge ---
            discount = get_text_safe(li, "div.plp-card-details-discount span.jm-badge")

            # --- quantity/weight ---
            # Sometimes shown separately:
            qty_sub = get_text_safe(li, "div.plp-card-details-sub")
            # Often embedded in the name as "... 85 g"
            qty = extract_quantity([qty_sub, name])

            # --- image ---
            # Prefer actual <img>, fall back to data-image on the anchor
            img_src = first_nonempty(
                get_attr_safe(li, "div.plp-card-image-wrapper img", "src"),
                get_attr_safe(li, "div.plp-card-image-wrapper img", "data-src"),
                root_a.get_attribute("data-image"),
            )

            # --- product url (nice to have) ---
            product_url = root_a.get_attribute("href") or ""

            # Clean small artifacts (e.g., currency spacing)
            price = price_raw.replace("\u20b9", "₹").strip()
            mrp = mrp_raw.replace("\u20b9", "₹").strip()

            data.append({
                "name": name,
                "image": img_src,
                "price": price,        # example: "₹33.00"
                "mrp": mrp,            # example: "₹50.00"
                "discount": discount,  # example: "34% OFF"
                "quantity_weight": qty,
                "product_url": product_url,
            })

        return pd.DataFrame(data)

    finally:
        driver.quit()

# ---------- Use on your page ----------
if __name__ == "__main__":
    url = "https://www.jiomart.com/c/groceries/biscuits-drinks-packaged-foods/chips-namkeens/29000"
    df = scrape_category(url, headless=True)
    print(f"Scraped {len(df)} products")
    df.to_csv("jiomart_chips_category.csv", index=False)
