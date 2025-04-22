# # # # import pandas as pd
# # # # import time
# # # # import pyautogui
# # # # from selenium import webdriver
# # # # from selenium.webdriver.common.by import By
# # # # from selenium.webdriver.chrome.service import Service
# # # # from selenium.webdriver.chrome.options import Options
# # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # from selenium.webdriver.support import expected_conditions as EC
# # # # from webdriver_manager.chrome import ChromeDriverManager

# # # # # Set up Selenium WebDriver (Headless)
# # # # options = Options()
# # # # options.add_argument("--headless")  # Run in headless mode (no browser window)
# # # # options.add_argument("--start-maximized")
# # # # options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # # Read Zepto URLs from CSV
# # # # review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\zepto_sub_categories.csv")

# # # # for i in range(len(review)):  
# # # #     url = review['URL'][i]
    
# # # #     try:
# # # #         driver.get(url)
# # # #         WebDriverWait(driver, 10).until(
# # # #             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
# # # #         )

# # # #         last_count = 0
# # # #         scroll_attempts = 0
# # # #         max_scroll_attempts = 15  # Prevent infinite loops

# # # #         while scroll_attempts < max_scroll_attempts:
# # # #             product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# # # #             new_count = len(product_cards)

# # # #             if new_count == last_count:  # No new products loaded
# # # #                 scroll_attempts += 1
# # # #             else:
# # # #                 scroll_attempts = 0  # Reset if new products appear

# # # #             last_count = new_count

# # # #             # **Use JavaScript for Scrolling (PyAutoGUI won't work in headless mode)**
# # # #             driver.execute_script("window.scrollBy(0, 500);")  # Scroll 500px down
# # # #             time.sleep(2)  # Give time for products to load

# # # #             try:
# # # #                 # Check if there is a "Load More" button
# # # #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# # # #                 if load_more.is_displayed():
# # # #                     load_more.click()
# # # #                     time.sleep(2)  # Allow time for new products to load
# # # #             except:
# # # #                 pass  # No "Load More" button, continue scrolling

# # # #         print(f"Total Products Found: {len(product_cards)}")

# # # #         # Extract product details
# # # #         for product in product_cards:
# # # #             try:
# # # #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# # # #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# # # #                 try:
# # # #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# # # #                 except:
# # # #                     discount = "No Discount"

# # # #                 print(f"Product: {name}, Price: {price}, Discount: {discount}")
# # # #             except Exception as e:
# # # #                 print("Error extracting product details:", e)

# # # #     except Exception as e:
# # # #         print("Error occurred:", e)

# # # #     print(f"Completed scraping for URL {i+1}/{len(review)}")

# # # # driver.quit()
# # # import pandas as pd
# # # import os
# # # import time
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # Set up Selenium WebDriver (Headless)
# # # options = Options()
# # # options.add_argument("--headless")  # Run in headless mode (no browser window)
# # # options.add_argument("--start-maximized")
# # # options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # Read Zepto URLs from CSV
# # # review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\zepto_sub_categories.csv")

# # # # List to store scraped data
# # # data = []

# # # for i in range(1):  
# # #     url = review['URL'][i]
    
# # #     try:
# # #         driver.get(url)
# # #         WebDriverWait(driver, 10).until(
# # #             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
# # #         )

# # #         last_count = 0
# # #         scroll_attempts = 0
# # #         max_scroll_attempts = 15  # Prevent infinite loops

# # #         while scroll_attempts < max_scroll_attempts:
# # #             product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# # #             new_count = len(product_cards)

# # #             if new_count == last_count:  # No new products loaded
# # #                 scroll_attempts += 1
# # #             else:
# # #                 scroll_attempts = 0  # Reset if new products appear

# # #             last_count = new_count

# # #             # Use JavaScript for scrolling
# # #             driver.execute_script("window.scrollBy(0, 500);")  # Scroll 500px down
# # #             time.sleep(2)  # Give time for products to load

# # #             try:
# # #                 # Click "Load More" button if present
# # #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# # #                 if load_more.is_displayed():
# # #                     load_more.click()
# # #                     time.sleep(2)  # Allow time for new products to load
# # #             except:
# # #                 pass  # No "Load More" button, continue scrolling

# # #         print(f"Total Products Found: {len(product_cards)}")

# # #         # Extract product details and save to list
# # #         for product in product_cards:
# # #             try:
# # #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# # #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# # #                 try:
# # #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# # #                 except:
# # #                     discount = "No Discount"

# # #                 # Append product data
# # #                 data.append([url, name, price, discount])

# # #             except Exception as e:
# # #                 print("Error extracting product details:", e)

# # #     except Exception as e:
# # #         print("Error occurred:", e)

# # #     print(f"Completed scraping for URL {i+1}/{len(review)}")

# # # # # Save data to CSV
# # # # df = pd.DataFrame(data, columns=["URL", "Product Name", "Price", "Discount"])
# # # # df.to_csv("zepto_products.csv", index=False, encoding="utf-8")
# # # # print("✅ Data saved to zepto_products.csv")
# # # df = pd.DataFrame(data, columns=["URL", "Product Name", "Price", "Discount"])

# # # # Define CSV file path
# # # csv_file = "zepto_products.csv"

# # # # Check if the file already exists
# # # file_exists = os.path.isfile(csv_file)

# # # # Append data to CSV (don't write header if file exists)
# # # df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# # # print("✅ Data appended to zepto_products.csv")
# # # driver.quit()
# # import pandas as pd
# # import os
# # import time
# # from datetime import datetime  # Import datetime for date handling
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager

# # # Get the current date and print it
# # current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # print(f"📅 Script Execution Date: {current_date}")

# # # Set up Selenium WebDriver (Headless)
# # options = Options()
# # options.add_argument("--headless")  # Run in headless mode (no browser window)
# # options.add_argument("--start-maximized")
# # options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # Read Zepto URLs from CSV
# # review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\zepto_sub_categories.csv")

# # # List to store scraped data
# # data = []

# # for i in range(1):  
# #     url = review['URL'][i]
    
# #     try:
# #         driver.get(url)
# #         WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
# #         )

# #         last_count = 0
# #         scroll_attempts = 0
# #         max_scroll_attempts = 15  # Prevent infinite loops

# #         while scroll_attempts < max_scroll_attempts:
# #             product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# #             new_count = len(product_cards)

# #             if new_count == last_count:  # No new products loaded
# #                 scroll_attempts += 1
# #             else:
# #                 scroll_attempts = 0  # Reset if new products appear

# #             last_count = new_count

# #             # Use JavaScript for scrolling
# #             driver.execute_script("window.scrollBy(0, 500);")  # Scroll 500px down
# #             time.sleep(2)  # Give time for products to load

# #             try:
# #                 # Click "Load More" button if present
# #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# #                 if load_more.is_displayed():
# #                     load_more.click()
# #                     time.sleep(2)  # Allow time for new products to load
# #             except:
# #                 pass  # No "Load More" button, continue scrolling

# #         print(f"Total Products Found: {len(product_cards)}")

# #         # Extract product details and save to list
# #         for product in product_cards:
# #             try:
# #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# #                 try:
# #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# #                 except:
# #                     discount = "No Discount"

# #                 # Append product data with date
# #                 data.append([current_date, url, name, price, discount])

# #             except Exception as e:
# #                 print("Error extracting product details:", e)

# #     except Exception as e:
# #         print("Error occurred:", e)

# #     print(f"✅ Completed scraping for URL {i+1}/{len(review)}")

# # # Save data to CSV with date column
# # df = pd.DataFrame(data, columns=["Date", "URL", "Product Name", "Price", "Discount"])

# # # Define CSV file path
# # csv_file = "zepto_products.csv"

# # # Check if the file already exists
# # file_exists = os.path.isfile(csv_file)

# # # Append data to CSV (don't write header if file exists)
# # df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# # print("✅ Data appended to zepto_products.csv")
# # driver.quit()
# import pandas as pd
# import os
# import time
# from datetime import datetime  # Import datetime for timestamp
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# # Get the current timestamp and print it
# current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
# print(f"📅 Script Execution Timestamp: {current_timestamp}")

# # Set up Selenium WebDriver (Headless)
# options = Options()
# options.add_argument("--headless")  # Run in headless mode (no browser window)
# options.add_argument("--start-maximized")
# options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Read Zepto URLs from CSV
# review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\zepto_sub_categories.csv")

# # List to store scraped data
# data = []

# for i in range(len(review)):  
#     url = review['URL'][i]
    
#     try:
#         driver.get(url)
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
#         )

#         last_count = 0
#         scroll_attempts = 0
#         max_scroll_attempts = 15  # Prevent infinite loops

#         while scroll_attempts < max_scroll_attempts:
#             product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
#             new_count = len(product_cards)

#             if new_count == last_count:  # No new products loaded
#                 scroll_attempts += 1
#             else:
#                 scroll_attempts = 0  # Reset if new products appear

#             last_count = new_count

#             # Use JavaScript for scrolling
#             driver.execute_script("window.scrollBy(0, 1000);")  # Scroll 500px down
#             time.sleep(2)  # Give time for products to load

#             try:
#                 # Click "Load More" button if present
#                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
#                 if load_more.is_displayed():
#                     load_more.click()
#                     time.sleep(2)  # Allow time for new products to load
#             except:
#                 pass  # No "Load More" button, continue scrolling

#         print(f"Total Products Found: {len(product_cards)}")

#         # Extract product details and save to list
#         for product in product_cards:
#             try:
#                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
#                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
#                 try:
#                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
#                 except:
#                     discount = "No Discount"

#                 # Append product data with timestamp
#                 data.append([current_timestamp, url, name, price, discount])

#             except Exception as e:
#                 print("Error extracting product details:", e)

#     except Exception as e:
#         print("Error occurred:", e)

#     print(f"✅ Completed scraping for URL {i+1}/{len(review)}")

# # Save data to CSV with timestamp column
# df = pd.DataFrame(data, columns=["Timestamp", "URL", "Name", "Price", "Discount"])

# # Define CSV file path
# csv_file = "zepto_products.csv"

# # Check if the file already exists
# file_exists = os.path.isfile(csv_file)

# # Append data to CSV (don't write header if file exists)
# df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# print("✅ Data appended to zepto_products.csv")
# driver.quit()
import pandas as pd
import os
import time
from datetime import datetime  # Import datetime for timestamp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Get the current timestamp and print it
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
print(f"📅 Script Execution Timestamp: {current_timestamp}")

# Set up Selenium WebDriver (Headless)
options = Options()
options.add_argument("--headless")  # Run in headless mode (no browser window)
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Read Zepto URLs from CSV
review = pd.read_csv(r"categories.csv")

# List to store scraped data
data = []

for i in range(len(review)):  
    url = review['zepto'][i]
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
        )

        last_count = 0
        scroll_attempts = 0
        max_scroll_attempts = 15  # Prevent infinite loops

        while scroll_attempts < max_scroll_attempts:
            product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
            new_count = len(product_cards)

            if new_count == last_count:  # No new products loaded
                scroll_attempts += 1
            else:
                scroll_attempts = 0  # Reset if new products appear

            last_count = new_count

            # Use JavaScript for scrolling
            driver.execute_script("window.scrollBy(0, 1000);")  # Scroll down
            time.sleep(2)  # Give time for products to load

            try:
                # Click "Load More" button if present
                load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
                if load_more.is_displayed():
                    load_more.click()
                    time.sleep(2)  # Allow time for new products to load
            except:
                pass  # No "Load More" button, continue scrolling

        # ✅ Re-fetch product cards AFTER scrolling completes
        product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
        print(f"🔍 Total Products Extracted: {len(product_cards)} from URL {i+1}/{len(review)}")

        # ✅ Extract product details correctly
        for product in product_cards:
            try:
                name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
                price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
                try:
                    discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
                except:
                    discount = "No Discount"
                try:
                    quantity = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-quantity"]').text
                except:
                    quantity = "N/A"  # Default if quantity is missing

                # Append product data with quantity included
                data.append([current_timestamp, url, name, price, discount, quantity])

            except Exception as e:
                print("⚠️ Error extracting product details:", e)

    except Exception as e:
        print(f"❌ Error scraping URL {i+1}/{len(review)}: {e}")

    print(f"✅ Completed scraping for URL {i+1}/{len(review)}\n")

# ✅ Save data to CSV with timestamp column
df = pd.DataFrame(data, columns=["Timestamp", "URL", "Name", "Price", "Discount", "Quantity"])

# Define CSV file path
csv_file = "zepto_products.csv"

# Check if the file already exists
file_exists = os.path.isfile(csv_file)

# Append data to CSV (don't write header if file exists)
df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

print("✅ Data successfully appended to zepto_products.csv")
driver.quit()
