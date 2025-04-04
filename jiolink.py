import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Setup Selenium WebDriver
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
# options.add_argument("--headless")  # Uncomment to run in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ✅ Open JioMart homepage
url = "https://www.jiomart.com/"
driver.get(url)
time.sleep(5)  # Allow time for page to load

# ✅ Get page source and close driver
html = driver.page_source
driver.quit()

# ✅ Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# ✅ Extract category links
categories = []
for link in soup.select("a[href^='/c/']"):  # Selecting category links
    category_name = link.text.strip()
    category_url = "https://www.jiomart.com" + link["href"]
    
    if category_name and category_url not in [c[1] for c in categories]:  # Avoid duplicates
        categories.append((category_name, category_url))

print(f"✅ Found {len(categories)} categories.")

# ✅ Save to CSV file
csv_filename = "jiomart_categories.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Category Name", "Category URL"])  # Headers
    writer.writerows(categories)

print(f"✅ Data saved to {csv_filename}")
