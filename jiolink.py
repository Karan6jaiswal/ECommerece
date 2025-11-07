# import csv
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # ✅ Setup Selenium WebDriver
# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-gpu")
# # options.add_argument("--headless")  # Uncomment to run in headless mode

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # ✅ Open JioMart homepage
# url = "https://www.jiomart.com/"
# driver.get(url)
# time.sleep(5)  # Allow time for page to load

# # ✅ Get page source and close driver
# html = driver.page_source
# driver.quit()

# # ✅ Parse with BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# # ✅ Extract category links
# categories = []
# for link in soup.select("a[href^='/c/']"):  # Selecting category links
#     category_name = link.text.strip()
#     category_url = "https://www.jiomart.com" + link["href"]
    
#     if category_name and category_url not in [c[1] for c in categories]:  # Avoid duplicates
#         categories.append((category_name, category_url))

# print(f"✅ Found {len(categories)} categories.")

# # ✅ Save to CSV file
# csv_filename = "jiomart_categories.csv"
# with open(csv_filename, "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Category Name", "Category URL"])  # Headers
#     writer.writerows(categories)

# print(f"✅ Data saved to {csv_filename}")
import csv, time, urllib.parse as urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

HOME = "https://www.jiomart.com/?tab=groceries"

def build_driver(headless=False):
    opts = Options()
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-gpu")
    if headless:
        opts.add_argument("--headless=new")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

def lazy_load_all(driver, max_rounds=20, pause=1.2):
    # wait for initial content
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    last_h = 0
    rounds = 0
    while rounds < max_rounds:
        rounds += 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)

        # try clicking any obvious "load more" containers
        for sel in [
            "[data-pages]",           # JioMart dynamic container seen in your screenshot
            ".dynamic_page_load_more",
            "[data-action='load-more']",
            "button.load_more, a.load_more",
        ]:
            elems = driver.find_elements(By.CSS_SELECTOR, sel)
            for e in elems:
                try:
                    driver.execute_script("arguments[0].click();", e)
                    time.sleep(0.8)
                except Exception:
                    pass

        new_h = driver.execute_script("return document.body.scrollHeight")
        if new_h == last_h:
            # one more small nudge to be sure
            driver.execute_script("window.scrollBy(0, -200);")
            time.sleep(0.4)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.8)
            new_h = driver.execute_script("return document.body.scrollHeight")
            if new_h == last_h:
                break
        last_h = new_h

def get_all_links(driver):
    # Use JS to extract every anchor href currently in DOM
    js = """
    return Array.from(document.querySelectorAll('a[href]'))
      .map(a => a.href)
      .filter(h => h && /^https?:\\/\\//i.test(h));
    """
    links = driver.execute_script(js)
    # Dedupe while preserving order
    seen, unique = set(), []
    for h in links:
        if h not in seen:
            seen.add(h); unique.append(h)
    return unique

def main():
    driver = build_driver(headless=False)
    driver.get(HOME)

    # Let critical sections render
    time.sleep(2.5)
    lazy_load_all(driver, max_rounds=25, pause=1.0)

    links = get_all_links(driver)
    driver.quit()

    # OPTIONAL: keep only jiomart domain (comment out to keep all)
    keep = []
    for h in links:
        parsed = urlparse.urlparse(h)
        if parsed.netloc.endswith("jiomart.com"):
            keep.append(h)

    print(f"Found {len(links)} total links; {len(keep)} on jiomart.com")

    # Save
    out = "jiomart_all_links.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["URL"])
        for h in keep:
            w.writerow([h])
    print(f"Saved to {out}")

if __name__ == "__main__":
    main()

