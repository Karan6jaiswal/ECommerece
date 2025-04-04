# import csv
# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# def setup_driver():
#     options = Options()
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-gpu")
#     return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# def get_category_links(driver, url):
#     driver.get(url)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     categories = soup.select("div.box-border.flex a.contents")
    
#     category_links = []
#     for cat in categories:
#         link = cat.get("href")
#         name = cat.text.strip() if cat.text else "Unknown"
#         if link and name:
#             full_link = f"https://www.zeptonow.com{link}" if not link.startswith("http") else link
#             category_links.append((name, full_link))
#     return category_links

# def get_sub_category_links(driver, category_links):
#     sub_category_data = []
    
#     for category_name, category_url in category_links:
#         driver.get(category_url)
#         time.sleep(3)
        
#         print(f"Processing Category: {category_name}")
#         link_elements = driver.find_elements(By.CSS_SELECTOR, "a.relative.mb-2.flex.cursor-pointer.items-center.p-2")
        
#         for link in link_elements:
#             sub_category_name = link.text.strip()
#             sub_category_url = link.get_attribute("href")
#             if sub_category_name and sub_category_url:
#                 sub_category_data.append((category_name, sub_category_name, sub_category_url))
#                 print(f"Found Sub-Category: {sub_category_name} -> {sub_category_url}")
    
#     return sub_category_data

# def save_to_csv(filename, data, headers):
#     with open(filename, "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(headers)
#         writer.writerows(data)
#     print(f"✅ Data saved to {filename}")

# if __name__ == "__main__":
#     driver = setup_driver()
#     main_url = "https://www.zeptonow.com/"
    
#     # Extract main categories
#     category_csv = "zepto_categories.csv"
#     category_links = get_category_links(driver, main_url)
#     save_to_csv(category_csv, category_links, ["Category Name", "URL"])
    
#     # Extract subcategories
#     sub_category_csv = "zepto_sub_categories.csv"
#     sub_category_links = get_sub_category_links(driver, category_links)
#     save_to_csv(sub_category_csv, sub_category_links, ["Main Category", "Sub-Category Name", "URL"])
    
#     driver.quit()
import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# ✅ Setup Chrome WebDriver
def setup_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ✅ Get Category Links
def get_category_links(driver, url):
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href^='/cn/']")))
    except:
        print("❌ No categories found or page load timeout.")
        return []

    soup = BeautifulSoup(driver.page_source, "html.parser")
    categories = soup.select("a[href^='/cn/']")  # Select category links
    
    category_links = []
    for cat in categories:
        link = cat.get("href")
        name = cat.text.strip() if cat.text else "Unknown"
        if link:
            full_link = f"https://www.zeptonow.com{link}"
            category_links.append((name, full_link))
    
    return category_links

# ✅ Get Sub-Category Links
def get_sub_category_links(driver, category_links):
    sub_category_data = []
    
    for category_name, category_url in category_links:
        driver.get(category_url)
        
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href^='/cn/']")))
        except:
            print(f"❌ No subcategories found for {category_name}")
            continue
        
        print(f"🔹 Processing Category: {category_name}")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        sub_categories = soup.select("a[href^='/cn/']")
        
        for sub in sub_categories:
            sub_category_name = sub.text.strip()
            sub_category_url = sub.get("href")
            if sub_category_name and sub_category_url:
                full_sub_category_url = f"https://www.zeptonow.com{sub_category_url}"
                sub_category_data.append((category_name, sub_category_name, full_sub_category_url))
                print(f"✅ Found: {sub_category_name} -> {full_sub_category_url}")
    
    return sub_category_data

# ✅ Save Data to CSV
def save_to_csv(filename, data, headers):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"📁 Data saved to {filename}")

# 🚀 Main Execution
if __name__ == "__main__":
    driver = setup_driver()
    main_url = "https://www.zeptonow.com/"
    
    # Extract Main Categories
    category_csv = "zepto_categories.csv"
    category_links = get_category_links(driver, main_url)
    save_to_csv(category_csv, category_links, ["Category Name", "URL"])
    
    # Extract Subcategories
    sub_category_csv = "zepto_sub_categories.csv"
    sub_category_links = get_sub_category_links(driver, category_links)
    save_to_csv(sub_category_csv, sub_category_links, ["Main Category", "Sub-Category Name", "URL"])
    
    driver.quit()
