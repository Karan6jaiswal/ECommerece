# # # # # # import pandas as pd
# # # # # # import time
# # # # # # import pyautogui
# # # # # # from selenium import webdriver
# # # # # # from selenium.webdriver.common.by import By
# # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # # from selenium.webdriver.support import expected_conditions as EC
# # # # # # from webdriver_manager.chrome import ChromeDriverManager

# # # # # # # Set up Selenium WebDriver (Headless)
# # # # # # options = Options()
# # # # # # options.add_argument("--headless")  # Run in headless mode (no browser window)
# # # # # # options.add_argument("--start-maximized")
# # # # # # options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# # # # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # # # # Read Zepto URLs from CSV
# # # # # # review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\zepto_sub_categories.csv")

# # # # # # for i in range(len(review)):  
# # # # # #     url = review['URL'][i]
    
# # # # # #     try:
# # # # # #         driver.get(url)
# # # # # #         WebDriverWait(driver, 10).until(
# # # # # #             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
# # # # # #         )

# # # # # #         last_count = 0
# # # # # #         scroll_attempts = 0
# # # # # #         max_scroll_attempts = 15  # Prevent infinite loops

# # # # # #         while scroll_attempts < max_scroll_attempts:
# # # # # #             product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# # # # # #             new_count = len(product_cards)

# # # # # #             if new_count == last_count:  # No new products loaded
# # # # # #                 scroll_attempts += 1
# # # # # #             else:
# # # # # #                 scroll_attempts = 0  # Reset if new products appear

# # # # # #             last_count = new_count

# # # # # #             # **Use JavaScript for Scrolling (PyAutoGUI won't work in headless mode)**
# # # # # #             driver.execute_script("window.scrollBy(0, 500);")  # Scroll 500px down
# # # # # #             time.sleep(2)  # Give time for products to load

# # # # # #             try:
# # # # # #                 # Check if there is a "Load More" button
# # # # # #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# # # # # #                 if load_more.is_displayed():
# # # # # #                     load_more.click()
# # # # # #                     time.sleep(2)  # Allow time for new products to load
# # # # # #             except:
# # # # # #                 pass  # No "Load More" button, continue scrolling

# # # # # #         print(f"Total Products Found: {len(product_cards)}")

# # # # # #         # Extract product details
# # # # # #         for product in product_cards:
# # # # # #             try:
# # # # # #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# # # # # #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# # # # # #                 try:
# # # # # #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# # # # # #                 except:
# # # # # #                     discount = "No Discount"

# # # # # #                 print(f"Product: {name}, Price: {price}, Discount: {discount}")
# # # # # #             except Exception as e:
# # # # # #                 print("Error extracting product details:", e)

# # # # # #     except Exception as e:
# # # # # #         print("Error occurred:", e)

# # # # # #     print(f"Completed scraping for URL {i+1}/{len(review)}")

# # # # # # driver.quit()
# # # # # import pandas as pd
# # # # # import os
# # # # # import time
# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.common.by import By
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.chrome.options import Options
# # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # from selenium.webdriver.support import expected_conditions as EC
# # # # # from webdriver_manager.chrome import ChromeDriverManager

# # # # # # Set up Selenium WebDriver (Headless)
# # # # # options = Options()
# # # # # options.add_argument("--headless")  # Run in headless mode (no browser window)
# # # # # options.add_argument("--start-maximized")
# # # # # options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# # # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # # # Read Zepto URLs from CSV
# # # # # review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\zepto_sub_categories.csv")

# # # # # # List to store scraped data
# # # # # data = []

# # # # # for i in range(1):  
# # # # #     url = review['URL'][i]
    
# # # # #     try:
# # # # #         driver.get(url)
# # # # #         WebDriverWait(driver, 10).until(
# # # # #             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
# # # # #         )

# # # # #         last_count = 0
# # # # #         scroll_attempts = 0
# # # # #         max_scroll_attempts = 15  # Prevent infinite loops

# # # # #         while scroll_attempts < max_scroll_attempts:
# # # # #             product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# # # # #             new_count = len(product_cards)

# # # # #             if new_count == last_count:  # No new products loaded
# # # # #                 scroll_attempts += 1
# # # # #             else:
# # # # #                 scroll_attempts = 0  # Reset if new products appear

# # # # #             last_count = new_count

# # # # #             # Use JavaScript for scrolling
# # # # #             driver.execute_script("window.scrollBy(0, 500);")  # Scroll 500px down
# # # # #             time.sleep(2)  # Give time for products to load

# # # # #             try:
# # # # #                 # Click "Load More" button if present
# # # # #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# # # # #                 if load_more.is_displayed():
# # # # #                     load_more.click()
# # # # #                     time.sleep(2)  # Allow time for new products to load
# # # # #             except:
# # # # #                 pass  # No "Load More" button, continue scrolling

# # # # #         print(f"Total Products Found: {len(product_cards)}")

# # # # #         # Extract product details and save to list
# # # # #         for product in product_cards:
# # # # #             try:
# # # # #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# # # # #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# # # # #                 try:
# # # # #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# # # # #                 except:
# # # # #                     discount = "No Discount"

# # # # #                 # Append product data
# # # # #                 data.append([url, name, price, discount])

# # # # #             except Exception as e:
# # # # #                 print("Error extracting product details:", e)

# # # # #     except Exception as e:
# # # # #         print("Error occurred:", e)

# # # # #     print(f"Completed scraping for URL {i+1}/{len(review)}")

# # # # # # # Save data to CSV
# # # # # # df = pd.DataFrame(data, columns=["URL", "Product Name", "Price", "Discount"])
# # # # # # df.to_csv("zepto_products.csv", index=False, encoding="utf-8")
# # # # # # print("✅ Data saved to zepto_products.csv")
# # # # # df = pd.DataFrame(data, columns=["URL", "Product Name", "Price", "Discount"])

# # # # # # Define CSV file path
# # # # # csv_file = "zepto_products.csv"

# # # # # # Check if the file already exists
# # # # # file_exists = os.path.isfile(csv_file)

# # # # # # Append data to CSV (don't write header if file exists)
# # # # # df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# # # # # print("✅ Data appended to zepto_products.csv")
# # # # # driver.quit()
# # # # import pandas as pd
# # # # import os
# # # # import time
# # # # from datetime import datetime  # Import datetime for date handling
# # # # from selenium import webdriver
# # # # from selenium.webdriver.common.by import By
# # # # from selenium.webdriver.chrome.service import Service
# # # # from selenium.webdriver.chrome.options import Options
# # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # from selenium.webdriver.support import expected_conditions as EC
# # # # from webdriver_manager.chrome import ChromeDriverManager

# # # # # Get the current date and print it
# # # # current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # # # print(f"📅 Script Execution Date: {current_date}")

# # # # # Set up Selenium WebDriver (Headless)
# # # # options = Options()
# # # # options.add_argument("--headless")  # Run in headless mode (no browser window)
# # # # options.add_argument("--start-maximized")
# # # # options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# # # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # # Read Zepto URLs from CSV
# # # # review = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\coding\zepto_sub_categories.csv")

# # # # # List to store scraped data
# # # # data = []

# # # # for i in range(1):  
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

# # # #             # Use JavaScript for scrolling
# # # #             driver.execute_script("window.scrollBy(0, 500);")  # Scroll 500px down
# # # #             time.sleep(2)  # Give time for products to load

# # # #             try:
# # # #                 # Click "Load More" button if present
# # # #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# # # #                 if load_more.is_displayed():
# # # #                     load_more.click()
# # # #                     time.sleep(2)  # Allow time for new products to load
# # # #             except:
# # # #                 pass  # No "Load More" button, continue scrolling

# # # #         print(f"Total Products Found: {len(product_cards)}")

# # # #         # Extract product details and save to list
# # # #         for product in product_cards:
# # # #             try:
# # # #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# # # #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# # # #                 try:
# # # #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# # # #                 except:
# # # #                     discount = "No Discount"

# # # #                 # Append product data with date
# # # #                 data.append([current_date, url, name, price, discount])

# # # #             except Exception as e:
# # # #                 print("Error extracting product details:", e)

# # # #     except Exception as e:
# # # #         print("Error occurred:", e)

# # # #     print(f"✅ Completed scraping for URL {i+1}/{len(review)}")

# # # # # Save data to CSV with date column
# # # # df = pd.DataFrame(data, columns=["Date", "URL", "Product Name", "Price", "Discount"])

# # # # # Define CSV file path
# # # # csv_file = "zepto_products.csv"

# # # # # Check if the file already exists
# # # # file_exists = os.path.isfile(csv_file)

# # # # # Append data to CSV (don't write header if file exists)
# # # # df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# # # # print("✅ Data appended to zepto_products.csv")
# # # # driver.quit()
# # # import pandas as pd
# # # import os
# # # import time
# # # from datetime import datetime  # Import datetime for timestamp
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # Get the current timestamp and print it
# # # current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
# # # print(f"📅 Script Execution Timestamp: {current_timestamp}")

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

# # # for i in range(len(review)):  
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
# # #             driver.execute_script("window.scrollBy(0, 1000);")  # Scroll 500px down
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

# # #                 # Append product data with timestamp
# # #                 data.append([current_timestamp, url, name, price, discount])

# # #             except Exception as e:
# # #                 print("Error extracting product details:", e)

# # #     except Exception as e:
# # #         print("Error occurred:", e)

# # #     print(f"✅ Completed scraping for URL {i+1}/{len(review)}")

# # # # Save data to CSV with timestamp column
# # # df = pd.DataFrame(data, columns=["Timestamp", "URL", "Name", "Price", "Discount"])

# # # # Define CSV file path
# # # csv_file = "zepto_products.csv"

# # # # Check if the file already exists
# # # file_exists = os.path.isfile(csv_file)

# # # # Append data to CSV (don't write header if file exists)
# # # df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# # # print("✅ Data appended to zepto_products.csv")
# # # driver.quit()
# # # import pandas as pd
# # # import os
# # # import time
# # # from datetime import datetime  # Import datetime for timestamp
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # Get the current timestamp and print it
# # # current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
# # # print(f"📅 Script Execution Timestamp: {current_timestamp}")

# # # # Set up Selenium WebDriver (Headless)
# # # options = Options()
# # # options.add_argument("--headless")  # Run in headless mode (no browser window)
# # # options.add_argument("--start-maximized")
# # # options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection
# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # # Read Zepto URLs from CSV
# # # review = pd.read_csv(r"categories.csv")

# # # # List to store scraped data
# # # data = []

# # # for i in range(len(review)):  
# # #     url = review['zepto'][i]
    
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
# # #             driver.execute_script("window.scrollBy(0, 1000);")  # Scroll down
# # #             time.sleep(2)  # Give time for products to load

# # #             try:
# # #                 # Click "Load More" button if present
# # #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# # #                 if load_more.is_displayed():
# # #                     load_more.click()
# # #                     time.sleep(2)  # Allow time for new products to load
# # #             except:
# # #                 pass  # No "Load More" button, continue scrolling

# # #         # ✅ Re-fetch product cards AFTER scrolling completes
# # #         product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# # #         print(f"🔍 Total Products Extracted: {len(product_cards)} from URL {i+1}/{len(review)}")

# # #         # ✅ Extract product details correctly
# # #         for product in product_cards:
# # #             try:
# # #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# # #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# # #                 try:
# # #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# # #                 except:
# # #                     discount = "No Discount"
# # #                 try:
# # #                     quantity = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-quantity"]').text
# # #                 except:
# # #                     quantity = "N/A"  # Default if quantity is missing

# # #                 # Append product data with quantity included
# # #                 data.append([current_timestamp, url, name, price, discount, quantity])

# # #             except Exception as e:
# # #                 print("⚠️ Error extracting product details:", e)

# # #     except Exception as e:
# # #         print(f"❌ Error scraping URL {i+1}/{len(review)}: {e}")

# # #     print(f"✅ Completed scraping for URL {i+1}/{len(review)}\n")

# # # # ✅ Save data to CSV with timestamp column
# # # df = pd.DataFrame(data, columns=["Timestamp", "URL", "Name", "Price", "Discount", "Quantity"])

# # # # Define CSV file path
# # # csv_file = "zepto_products.csv"

# # # # Check if the file already exists
# # # file_exists = os.path.isfile(csv_file)

# # # # Append data to CSV (don't write header if file exists)
# # # df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# # # print("✅ Data successfully appended to zepto_products.csv")
# # # driver.quit()
# # import pandas as pd
# # import os
# # import time
# # from datetime import datetime
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from webdriver_manager.chrome import ChromeDriverManager

# # # Get current timestamp
# # current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # print(f"📅 Script Execution Timestamp: {current_timestamp}")

# # # Set up Selenium WebDriver (Headless)
# # options = Options()
# # options.add_argument("--headless")
# # options.add_argument("--start-maximized")
# # options.add_argument("--disable-blink-features=AutomationControlled")

# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # # Read Zepto URLs from CSV
# # try:
# #     review = pd.read_csv("categories.csv")
# #     if 'zepto' not in review.columns:
# #         raise KeyError("Missing 'zepto' column in categories.csv")

# #     # Filter out invalid/missing URLs
# #     review = review[pd.notna(review['zepto']) & review['zepto'].str.startswith('http')].reset_index(drop=True)

# # except Exception as e:
# #     print(f"❌ Error reading 'categories.csv': {e}")
# #     driver.quit()
# #     exit()

# # # List to store scraped data
# # data = []

# # # Scrape each URL
# # for i in range(len(review)):
# #     url = review['zepto'][i]
# #     print(f"➡️ Scraping URL {i+1}/{len(review)}: {url}")

# #     try:
# #         driver.get(url)
# #         WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-card"]'))
# #         )

# #         last_count = 0
# #         scroll_attempts = 0
# #         max_scroll_attempts = 15

# #         while scroll_attempts < max_scroll_attempts:
# #             product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# #             new_count = len(product_cards)

# #             if new_count == last_count:
# #                 scroll_attempts += 1
# #             else:
# #                 scroll_attempts = 0

# #             last_count = new_count
# #             driver.execute_script("window.scrollBy(0, 1000);")
# #             time.sleep(2)

# #             try:
# #                 load_more = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
# #                 if load_more.is_displayed():
# #                     load_more.click()
# #                     time.sleep(2)
# #             except:
# #                 pass

# #         product_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
# #         print(f"🔍 Total Products Extracted: {len(product_cards)}")

# #         for product in product_cards:
# #             try:
# #                 name = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-name"]').text
# #                 price = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-price"]').text
# #                 try:
# #                     discount = product.find_element(By.CSS_SELECTOR, 'p.absolute.top-0.text-center').text
# #                 except:
# #                     discount = "No Discount"
# #                 try:
# #                     quantity = product.find_element(By.CSS_SELECTOR, '[data-testid="product-card-quantity"]').text
# #                 except:
# #                     quantity = "N/A"

# #                 data.append([current_timestamp, url, name, price, discount, quantity])
# #             except Exception as e:
# #                 print("⚠️ Error extracting product details:", e)

# #     except Exception as e:
# #         print(f"❌ Error scraping URL {i+1}/{len(review)}: {e}")

# #     print(f"✅ Completed scraping for URL {i+1}/{len(review)}\n")

# # # Save to CSV
# # df = pd.DataFrame(data, columns=["Timestamp", "URL", "Name", "Price", "Discount", "Quantity"])
# # csv_file = "zepto_products.csv"
# # file_exists = os.path.isfile(csv_file)
# # df.to_csv(csv_file, mode="a", index=False, encoding="utf-8", header=not file_exists)

# # print("✅ Data successfully appended to zepto_products.csv")
# # driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # --- Setup WebDriver ---
# options = Options()
# #options.add_argument("--headless")  # comment this if you want to see browser actions
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(options=options)

# # --- Target URL ---
# url = "https://www.zeptonow.com/cn/fruits-vegetables/fresh-fruits/cid/64374cfe-d06f-4a01-898e-c07c46462c36/scid/09e63c15-e5f7-4712-9ff8-513250b79942"
# driver.get(url)
# time.sleep(5)  # allow page to load

# # --- Scroll gradually by half of current height ---
# def scroll_halfway(driver, pause=1.0, max_idle_rounds=6):
#     """Scroll by half the page height until no new content loads."""
#     idle_rounds = 0
#     prev_height = 0

#     while True:
#         # Scroll down by 600 pixels
#         driver.execute_script("window.scrollBy(0, 600);")
#         time.sleep(0.6)
        
#         # Scroll back slightly by 200 pixels (to trigger lazy load)
#         driver.execute_script("window.scrollBy(0, -200);")
#         time.sleep(0.4)
        
#         # Check if new content loaded
#         new_height = driver.execute_script("return document.body.scrollHeight")
        
#         if new_height == prev_height:
#             idle_rounds += 1
#         else:
#             idle_rounds = 0
        
#         # Stop if no new content after several rounds
#         if idle_rounds >= 6:
#             break
        
#         prev_height = new_height

# scroll_halfway(driver)

# # --- Parse page source ---
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # find all product cards
# products = soup.find_all('a', href=lambda x: x and x.startswith('/pn/'))
# print(f"Total products found: {len(products)}")

# data = []
# for product in products:
#     # Product name
#     name_tag = product.find('div', {'data-slot-id': 'ProductName'})
#     name = name_tag.get_text(strip=True) if name_tag else None

#     # Quantity / weight
#     qty_tag = product.find('div', {'data-slot-id': 'PackSize'})
#     quantity = qty_tag.get_text(strip=True) if qty_tag else None

#     # Price (₹)
#     price_tag = product.find('span', {'class': 'cptQT7'})
#     price = price_tag.get_text(strip=True).replace('₹', '') if price_tag else None

#     # Original price (₹)
#     old_price_tag = product.find('span', {'class': 'cx3iWL'})
#     old_price = old_price_tag.get_text(strip=True).replace('₹', '') if old_price_tag else None

#     # Discount
#     discount_tag = product.find('div', {'class': 'c0aYst c1IV3p'})
#     discount = discount_tag.get_text(strip=True) if discount_tag else None

#     # Image link
#     img_tag = product.find('img')
#     img_link = img_tag['src'] if img_tag and img_tag.has_attr('src') else None

#     data.append({
#         'Product Name': name,
#         'Quantity': quantity,
#         'Price (₹)': price,
#         'Original Price (₹)': old_price,
#         'Discount': discount,
#         'Image Link': img_link
#     })

# driver.quit()

# # --- Save results ---
# df = pd.DataFrame(data)
# df.to_csv('zepto_fresh_fruits.csv', index=False)
# print(f"✅ Saved {len(df)} products to zepto_fresh_fruits.csv")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time, re, pandas as pd
from urllib.parse import urljoin

# ---------------------
# CONFIG
# ---------------------
CATEGORY_URL = "https://www.zeptonow.com/cn/fruits-vegetables/fresh-fruits/cid/64374cfe-d06f-4a01-898e-c07c46462c36/scid/09e63c15-e5f7-4712-9ff8-513250b79942"
BASE = "https://www.zeptonow.com"

options = Options()
# options.add_argument("--headless=new")         # uncomment for headless
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119 Safari/537.36")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

def scroll_until_done(pause=0.8, idle_rounds=6):
    """
    Scrolls to the bottom repeatedly until product count stops increasing
    for 'idle_rounds' iterations.
    """
    last_count = 0
    idle = 0
    while True:
        # Count anchors that wrap product cards (pattern you showed: /pn/<slug>/pvid/...)
        cards = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/pn/"]')
        count = len(cards)
        if count > last_count:
            idle = 0
            last_count = count
        else:
            idle += 1
            if idle >= idle_rounds:
                break
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        # nudge up a bit to trigger more lazy loads
        driver.execute_script("window.scrollBy(0, -300);")
        time.sleep(0.25)

def get_text_safe(root, css, default=""):
    try:
        el = root.find_element(By.CSS_SELECTOR, css)
        return el.text.strip()
    except NoSuchElementException:
        return default

def get_attr_safe(root, css, attr, default=""):
    try:
        el = root.find_element(By.CSS_SELECTOR, css)
        val = el.get_attribute(attr)
        return val if val is not None else default
    except NoSuchElementException:
        return default

def parse_price_block(root):
    """
    Prefer data-slot-id='EdlpPrice' for the current price.
    Capture MRP if present (often shown nearby).
    Also grab discount text if 'OFF' is present in the price area.
    """
    price_text = ""
    mrp_text = ""
    discount_text = ""

    # Current price (EDLP)
    price_el_text = get_text_safe(root, '[data-slot-id="EdlpPrice"]')
    if not price_el_text:
        price_el_text = get_text_safe(root, '[data-slot-id="Price"]')  # fallback

    price_text = price_el_text.replace("\n", " ").strip()

    # Try grabbing MRP / CompareAt if present
    # (Zepto sometimes uses a different slot; we’ll probe common ones)
    mrp_text = (
        get_text_safe(root, '[data-slot-id="CompareAtPrice"]') or
        get_text_safe(root, '[data-slot-id="Mrp"]')
    ).replace("\n", " ").strip()

    # Discount “₹13 OFF” usually sits near price (span with “OFF” text)
    # Look for any descendant containing OFF
    try:
        off_el = root.find_element(By.XPATH, './/*[contains(normalize-space(.), "OFF")]')
        discount_text = off_el.text.strip()
    except NoSuchElementException:
        discount_text = ""

    # Normalize numeric current price (₹ may be separated into multiple spans)
    def extract_rupees(s):
        m = re.search(r'₹\s*([0-9]+(?:\.[0-9]+)?)', s)
        return m.group(1) if m else ""

    cur_price_num = extract_rupees(price_text)
    mrp_num = extract_rupees(mrp_text)

    return cur_price_num, mrp_num, discount_text, price_text

def get_image_src(root):
    # within ProductImageWrapper -> img
    # try src, then data-src, then srcset first candidate
    try:
        img = root.find_element(By.CSS_SELECTOR, '[data-slot-id="ProductImageWrapper"] img')
        src = img.get_attribute("src") or ""
        if not src:
            src = img.get_attribute("data-src") or ""
        if not src:
            srcset = img.get_attribute("srcset") or ""
            if srcset:
                src = srcset.split(",")[0].split()[0]
        return src
    except NoSuchElementException:
        return ""

# ---------------------
# RUN
# ---------------------
driver.get(CATEGORY_URL)

# wait for any product to appear
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/pn/"]')))

# load everything
scroll_until_done(pause=0.8, idle_rounds=6)

products = []
seen_hrefs = set()

# After scrolling, snapshot the elements to avoid stale references while iterating
card_anchors = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/pn/"]')

for a in card_anchors:
    try:
        href = a.get_attribute("href") or a.get_attribute("data-href") or a.get_attribute("pathname") or ""
        if href and href.startswith("/"):
            href = urljoin(BASE, href)

        # Out-of-stock flag lives on the inner card div (data-is-out-of-stock="true|false")
        oos = ""
        try:
            inner = a.find_element(By.CSS_SELECTOR, '[data-is-out-of-stock]')
            oos = inner.get_attribute("data-is-out-of-stock") or ""
        except NoSuchElementException:
            oos = ""

        name = get_text_safe(a, '[data-slot-id="ProductName"]')
        pack = get_text_safe(a, '[data-slot-id="PackSize"]')
        cur_price, mrp, discount_text, raw_price_text = parse_price_block(a)
        img = get_image_src(a)

        # De-dup repeated anchors (sometimes same card appears twice during load)
        key = (href, name, pack)
        if key in seen_hrefs:
            continue
        seen_hrefs.add(key)

        products.append({
            "name": name,
            "pack_size": pack,
            "price_rs": cur_price,
            "mrp_rs": mrp,
            "discount_text": discount_text,   # e.g., "₹13 OFF"
            "out_of_stock": oos,              # "true"/"false"
            "img_url": img,
            "product_url": href,
            "raw_price_block": raw_price_text # helpful for debugging
        })
    except StaleElementReferenceException:
        # Skip if the card went stale during iteration
        continue

driver.quit()

# Save to CSV
df = pd.DataFrame(products)
df.to_csv("zepto_fruits.csv", index=False)
print(f"Extracted {len(df)} products and saved to zepto_fruits.csv")
