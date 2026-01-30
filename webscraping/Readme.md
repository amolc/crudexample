# 🕸️ Web Scraping with Python

This module covers the end-to-end process of extracting data from the web using Python. You will learn to handle both static and dynamic websites, process the extracted data, and follow ethical scraping practices.

---

## 🎯 Course Objectives
- Master **BeautifulSoup** for static HTML parsing.
- Use **Selenium** for scraping dynamic, JavaScript-heavy websites.
- Learn advanced data extraction using **CSS Selectors** and **XPath**.
- Store scraped data in **CSV**, **Pandas DataFrames**, and **SQLite**.
- Understand the **Legal & Ethical** aspects of web scraping.

---

## 🧩 Module-Wise Structure

### 🟦 MODULE 1: HTML Parsing with BeautifulSoup
BeautifulSoup is the industry standard for parsing and navigating static HTML content.

**Example: Scraping a static webpage**
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract page title
print("Title:", soup.title.text)

# Extract all links
for link in soup.find_all("a"):
    print(link.get("href"))
```

**Common Operations:**
```python
# Find elements by class
items = soup.find_all("div", class_="product")

# Find element by ID
header = soup.find(id="main-header")

# Extract clean text
for item in items:
    print(item.get_text(strip=True))
```

### 🟦 MODULE 2: Selenium for Dynamic Content
Selenium automates web browsers, making it essential for scraping websites that load content via JavaScript.

**Example: Basic Selenium scraping**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com")

time.sleep(3)  # wait for page to load

headings = driver.find_elements(By.TAG_NAME, "h2")
for h in headings:
    print(h.text)

driver.quit()
```

**Explicit Waits (Best Practice):**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
price = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "price"))
)
print(price.text)
```

### 🟦 MODULE 3: Data Extraction Techniques
Advanced methods to pinpoint specific data points.

- **CSS Selectors:**
  ```python
  products = soup.select(".product-item")
  for product in products:
      name = product.select_one(".name").text
      price = product.select_one(".price").text
      print(name, price)
  ```
- **XPath (Selenium):**
  ```python
  elements = driver.find_elements(By.XPATH, "//div[@class='product']")
  for el in elements:
      print(el.text)
  ```
- **Handling Pagination:**
  ```python
  page = 1
  while page <= 3:
      url = f"https://example.com/products?page={page}"
      response = requests.get(url)
      # ... process page ...
      page += 1
  ```

### 🟦 MODULE 4: Processing and Storing Data
Extracted data is only useful if it's stored correctly.

- **CSV Export:**
  ```python
  import csv
  data = [["Product A", "₹100"], ["Product B", "₹200"]]
  with open("products.csv", "w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["Name", "Price"])
      writer.writerows(data)
  ```
- **Pandas Integration:**
  ```python
  import pandas as pd
  df = pd.read_csv("products.csv")
  df["Price"] = df["Price"].str.replace("₹", "").astype(int)
  ```
- **SQLite Database:**
  ```python
  import sqlite3
  conn = sqlite3.connect("scraped_data.db")
  cursor = conn.cursor()
  cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Product A", 100))
  conn.commit()
  ```

### 🟦 MODULE 5: Legal and Ethical Considerations
Responsible scraping ensures your scripts don't get blocked or face legal issues.

- **Check `robots.txt`:**
  ```python
  import requests
  print(requests.get("https://example.com/robots.txt").text)
  ```
- **Polite Scraping:**
  ```python
  import time
  # Always use a User-Agent and rate limiting
  headers = {"User-Agent": "Mozilla/5.0"}
  time.sleep(2) # Be kind to servers
  ```

**Best Practices Checklist:**
- [ ] Respect `robots.txt`
- [ ] Follow Website Terms of Service
- [ ] Avoid scraping personal or sensitive data
- [ ] Use rate limiting and proper headers

---

Happy Scraping! 🚀
