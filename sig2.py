# # import pandas as pd
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time

# # # Set up Selenium WebDriver
# # options = Options()
# # options.add_argument("--start-maximized")
# # options.add_argument("--headless")  # Uncomment to run headless
# # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36")

# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # List to store product data
# # product_data = []

# # try:
# #     url = "https://www.swiggy.com/instamart/category-listing?categoryName=Tea%2C+Coffee+and+More&custom_back=true&taxonomyType=Speciality+taxonomy+1"
# #     driver.get(url)

# #     # Wait for initial products to load
# #     WebDriverWait(driver, 10).until(
# #         EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="ItemWidgetContainer"]'))
# #     )

# #     # Scroll down using JavaScript and wait for products to load
# #     last_height = driver.execute_script("return document.body.scrollHeight")
    
# #     while True:
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(2)  # Wait for new products to load
        
# #         new_height = driver.execute_script("return document.body.scrollHeight")
        
# #         if new_height == last_height:
# #             break  # Stop when no new content is loaded
# #         last_height = new_height

# #     # Get product cards after scrolling
# #     product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="ItemWidgetContainer"]')

# #     for product in product_cards:
# #         try:
# #             # Extract name
# #             name = product.find_element(By.CSS_SELECTOR, 'div[aria-label]').get_attribute('aria-label')

# #             # Extract prices
# #             try:
# #                 mrp_price = product.find_element(By.CSS_SELECTOR, 'div[data-testid="itemMRPPrice"]').text.strip()
# #             except:
# #                 mrp_price = "Not Available"

# #             try:
# #                 offer_price = product.find_element(By.CSS_SELECTOR, 'div[data-testid="itemOfferPrice"]').text.strip()
# #             except:
# #                 offer_price = "Not Available"

# #             # Extract weight/quantity
# #             try:
# #                 weight = product.find_element(By.CSS_SELECTOR, 'div[class*="entQHA"]').text.strip()
# #             except:
# #                 weight = "Not Specified"

# #             # Append as a single-line comma-separated format
# #             product_data.append(f"{name},{mrp_price},{offer_price},{weight}")

# #         except Exception as e:
# #             print("Error extracting product details:", e)

# # except Exception as e:
# #     print("Error occurred:", e)

# # finally:
# #     driver.quit()
    
# #     # Save to CSV (single-line format)
# #     with open("swiggy_products.csv", "w", encoding="utf-8") as file:
# #         file.write("Product Name,MRP Price,Offer Price,Weight\n")  # Header
# #         for row in product_data:
# #             file.write(row + "\n")  # Write each product in a single line

# #     print(f"✅ Data saved to swiggy_products.csv ({len(product_data)} products extracted)")



# # # import csv
# # # import time
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from bs4 import BeautifulSoup
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # ✅ Setup Selenium WebDriver
# # # options = Options()
# # # options.add_argument("--disable-blink-features=AutomationControlled")
# # # options.add_argument("--start-maximized")
# # # options.add_argument("--disable-gpu")
# # # # options.add_argument("--headless")  # Uncomment to run in headless mode

# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # ✅ Open Swiggy Instamart URL
# # # url = "https://www.swiggy.com/instamart/category-listing?categoryName=Tea%2C+Coffee+and+More&custom_back=true&taxonomyType=Speciality+taxonomy+1"
# # # driver.get(url)
# # # time.sleep(5)  # Allow time for page to load

# # # # ✅ Get page source and close driver
# # # html = driver.page_source
# # # driver.quit()

# # # # ✅ Parse with BeautifulSoup
# # # soup = BeautifulSoup(html, "html.parser")

# # # # ✅ Extract product details
# # # products = []
# # # for product in soup.select("[data-testid='ItemWidgetContainer']"):
# # #     name_tag = product.select_one("[aria-label]")  # Product Name
# # #     price_tag = product.select_one("[data-testid='itemMRPPrice']")  # Price
# # #     img_tag = product.select_one("button img")  # Product Image
# # #     quantity_tag = product.select_one("[aria-label]")  # Quantity (if available)

# # #     name = name_tag.text.strip() if name_tag else "N/A"
# # #     price = price_tag.text.strip() if price_tag else "N/A"
# # #     img_url = img_tag["src"] if img_tag else "N/A"
# # #     quantity = quantity_tag["aria-label"] if quantity_tag else "N/A"

# # #     products.append((name, price, quantity, img_url))

# # # print(f"✅ Found {len(products)} products.")

# # # # ✅ Save to CSV file
# # # csv_filename = "swiggy_instamart_products.csv"
# # # with open(csv_filename, "w", newline="", encoding="utf-8") as file:
# # #     writer = csv.writer(file)
# # #     writer.writerow(["Product Name", "Price", "Quantity", "Image URL"])  # Headers
# # #     writer.writerows(products)

# # # print(f"✅ Data saved to {csv_filename}")

# import csv
# import time
# import pyautogui
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager

# # Setup Selenium WebDriver
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-gpu")
# # options.add_argument("--headless")  # Uncomment for headless mode

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# review=pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\swigcat.csv")
# print(len(review))
# # Open Swiggy Instamart URL
# for i in range(1,len(review)):
    
    
#     url = review['URL'][i]
#     driver.get(url)

# # ✅ Wait until products load
#     try:
#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="ItemWidgetContainer"]'))
#         )
#     except Exception as e:
#         print("❌ Page did not load properly:", e)
#         driver.quit()
#         exit()

#     # ✅ Scroll automatically using pyautogui
#     scroll_attempts = 0
#     max_attempts = 15  # Maximum attempts to prevent infinite loop
#     previous_product_count = 0  # Track product count

#     time.sleep(2)  # Allow initial elements to render
#     while scroll_attempts < max_attempts:
#         pyautogui.scroll(-10000)  # Scroll down in smaller steps
#         time.sleep(2)  # Allow new elements to load
        
#         # Get current product count
#         html = driver.page_source
#         soup = BeautifulSoup(html, "html.parser")
#         products = soup.select('div[data-testid="ItemWidgetContainer"]')
#         current_product_count = len(products)

#         if current_product_count == previous_product_count:
#             scroll_attempts += 1  # Increase attempts if no new products load
#         else:
#             scroll_attempts = 0  # Reset attempts if new products appear

#         previous_product_count = current_product_count

#     # ✅ Parse final page source
#     soup = BeautifulSoup(driver.page_source, "html.parser")

#     # ✅ Extract product details
#     products = soup.select('div[data-testid="ItemWidgetContainer"]')
#     print(f"✅ Found {len(products)} products")

#     # ✅ CSV File Setup
#     csv_filename = "swiggy_products.csv"
#     with open(csv_filename, "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Product Name", "Price"])  # CSV Headers

#         for product in products:
#             try:
#                 name = product.select_one("div.novMV").text.strip()  # Product Name
#                 price = product.select_one("div[data-testid='itemOfferPrice']").text.strip()  # Product Price
                
#                 # Write to CSV
#                 writer.writerow([name, price])

#                 # Print Output
#                 print(f"Product: {name}")
#                 print(f"Price: {price}")
                
#                 print("-" * 40)

#             except Exception as e:
#                 print("❌ Error extracting product details:", e)

# # ✅ Close Selenium
# driver.quit()
# print(f"✅ Data saved to {csv_filename}")
# import csv
# import time
# import pyautogui
# import pandas as pd
# from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# # import os

# # Setup Selenium WebDriver
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-gpu")
# # options.add_argument("--headless")  # Uncomment for headless mode

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Read Swiggy URLs from CSV
# review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\swiggy_category.csv")
# print(f"✅ {len(review)} URLs found")

# # CSV File Setup
# csv_filename = "swiggy_products.csv"
# # file_exists = os.path.isfile(csv_filename)  # Check if file already exists

# with open(csv_filename, "a", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
    
#     # Write headers only if file does not exist
    
#     writer.writerow(["Timestamp", "Product Name", "Price", "URL"])

#     # Process each URL
#     for i in range(5):
#         url = review['URL'][i]
#         driver.get(url)

#         # ✅ Wait until products load
#         try:
#             WebDriverWait(driver, 30).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="ItemWidgetContainer"]'))
#             )
#         except Exception as e:
#             print(f"❌ Page did not load properly ({url}):", e)
#             continue

#         # ✅ Scroll to load all products
#         scroll_attempts = 0
#         max_attempts = 15
#         previous_product_count = 0

#         time.sleep(2)  # Allow initial elements to render
#         while scroll_attempts < max_attempts:
#             pyautogui.scroll(-10000)  # Scroll down
#             time.sleep(2)  # Allow new elements to load
            
#             # Get current product count
#             html = driver.page_source
#             soup = BeautifulSoup(html, "html.parser")
#             products = soup.select('div[data-testid="ItemWidgetContainer"]')
#             current_product_count = len(products)

#             if current_product_count == previous_product_count:
#                 scroll_attempts += 1
#             else:
#                 scroll_attempts = 0

#             previous_product_count = current_product_count

#         # ✅ Parse final page source
#         soup = BeautifulSoup(driver.page_source, "html.parser")

#         # ✅ Extract product details
#         products = soup.select('div[data-testid="ItemWidgetContainer"]')
#         print(f"✅ {len(products)} products found on {url}")

#         # ✅ Save data with timestamp
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         for product in products:
#             try:
#                 name = product.select_one("div.novMV").text.strip()  # Product Name
#                 price = product.select_one("div[data-testid='itemOfferPrice']").text.strip()  # Product Price
                
#                 # Write to CSV
#                 writer.writerow([timestamp, name, price, url])

#                 # Print Output
#                 print(f"Product: {name} | Price: {price}")
#                 print("-" * 40)

#             except Exception as e:
#                 print("❌ Error extracting product details:", e)

# # ✅ Close Selenium
# driver.quit()
# print(f"✅ Data appended to {csv_filename}")
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
review = pd.read_csv(r"C:\Users\admin\Desktop\Python\categories.csv")

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
