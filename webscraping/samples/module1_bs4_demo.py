import requests
from bs4 import BeautifulSoup

def demo_bs4_static_scraping():
    """
    Demonstrates scraping a static website (example.com) using BeautifulSoup.
    """
    print("--- 1. BeautifulSoup Static Scraping Demo ---")
    
    url = "https://example.com"
    try:
        # Step 1: Send a GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise error for bad status codes
        
        # Step 2: Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Step 3: Extract basic info
        print(f"Page Title: {soup.title.string}")
        
        # Step 4: Extract the main heading (h1)
        h1 = soup.find("h1")
        if h1:
            print(f"Main Heading: {h1.get_text()}")
            
        # Step 5: Extract the first paragraph
        p = soup.find("p")
        if p:
            print(f"First Paragraph: {p.get_text(strip=True)}")
            
        # Step 6: Find all links
        links = soup.find_all("a")
        print(f"Found {len(links)} link(s):")
        for link in links:
            print(f" - {link.get('href')}")
            
    except Exception as e:
        print(f"Error during scraping: {e}")
    print("-" * 45)

if __name__ == "__main__":
    demo_bs4_static_scraping()
