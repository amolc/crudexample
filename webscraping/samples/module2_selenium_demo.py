from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def demo_selenium_dynamic_scraping():
    """
    Demonstrates basic Selenium usage with Headless Chrome.
    Note: Requires Chrome browser installed on the system.
    """
    print("--- 2. Selenium Dynamic Scraping Demo ---")
    
    # Configure Chrome Options for Headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Run without a UI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Initialize the driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Step 1: Navigate to a website
        url = "https://www.google.com"
        print(f"Navigating to {url}...")
        driver.get(url)
        
        # Step 2: Explicit Wait for an element (e.g., the search box)
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        
        # Step 3: Extract information
        print(f"Page Title: {driver.title}")
        
        # Step 4: Interact with the page (optional demo)
        print("Search box found via Selenium.")
        
    except Exception as e:
        print(f"Selenium Error: {e}")
    finally:
        # Always close the browser
        driver.quit()
        print("Browser closed.")
    print("-" * 45)

if __name__ == "__main__":
    demo_selenium_dynamic_scraping()
