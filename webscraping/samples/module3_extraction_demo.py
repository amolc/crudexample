from bs4 import BeautifulSoup
import requests

def demo_advanced_extraction():
    """
    Demonstrates CSS Selectors and XPath-like selection logic.
    We'll use a local HTML string to simulate a complex product page.
    """
    print("--- 3. Data Extraction Techniques Demo ---")
    
    html_doc = """
    <html>
        <body>
            <div id="product-list">
                <div class="product-item" data-id="101">
                    <h3 class="name">Wireless Mouse</h3>
                    <span class="price">₹499</span>
                    <p class="description">Ergonomic 2.4G mouse.</p>
                </div>
                <div class="product-item" data-id="102">
                    <h3 class="name">Mechanical Keyboard</h3>
                    <span class="price">₹2,499</span>
                    <p class="description">RGB backlit keys.</p>
                </div>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, "html.parser")
    
    # 1. CSS Selectors (select and select_one)
    print("Extracting via CSS Selectors (.product-item):")
    products = soup.select(".product-item")
    for product in products:
        name = product.select_one(".name").text
        price = product.select_one(".price").text
        pid = product.get("data-id")
        print(f" - [{pid}] {name}: {price}")
        
    # 2. Handling Pagination (Logic Demo)
    print("\nPagination Logic (Simulation):")
    base_url = "https://example.com/shop?page="
    for page in range(1, 3):
        url = f"{base_url}{page}"
        print(f" - Generating URL for Page {page}: {url}")

    print("-" * 45)

if __name__ == "__main__":
    demo_advanced_extraction()
