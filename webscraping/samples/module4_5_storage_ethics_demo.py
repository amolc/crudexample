import csv
import sqlite3
import pandas as pd
import requests
import time
import os

def demo_storage_and_ethics():
    """
    Demonstrates storing data (CSV/SQLite) and checking robots.txt for ethics.
    """
    print("--- 4 & 5. Storage and Ethics Demo ---")
    
    data = [
        {"id": 1, "name": "Python Book", "price": 450},
        {"id": 2, "name": "Django Guide", "price": 550},
        {"id": 3, "name": "Flask Basics", "price": 300}
    ]
    
    # 1. Store in CSV
    csv_file = "scraped_data_demo.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "price"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {csv_file}")
    
    # 2. Store in SQLite
    db_file = "scraped_demo.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("CREATE TABLE books (id INTEGER, name TEXT, price INTEGER)")
    for item in data:
        cursor.execute("INSERT INTO books VALUES (?, ?, ?)", (item["id"], item["name"], item["price"]))
    conn.commit()
    conn.close()
    print(f"Data saved to SQLite: {db_file}")
    
    # 3. Ethics: Checking robots.txt
    print("\nEthics: Checking robots.txt for 'python.org'...")
    try:
        r = requests.get("https://www.python.org/robots.txt", timeout=5)
        print("First 5 lines of robots.txt:")
        print("\n".join(r.text.splitlines()[:5]))
    except:
        print("Could not fetch robots.txt")

    # 4. Rate Limiting (Demo)
    print("\nRate Limiting Example:")
    print(" - Request 1 sent...")
    time.sleep(1) # Sleep for 1 second between requests
    print(" - Request 2 sent after 1s delay.")

    # Cleanup demo files
    if os.path.exists(csv_file): os.remove(csv_file)
    if os.path.exists(db_file): os.remove(db_file)
    
    print("-" * 45)

if __name__ == "__main__":
    demo_storage_and_ethics()
