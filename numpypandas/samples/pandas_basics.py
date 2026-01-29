import pandas as pd
import numpy as np

def demo_pandas_series():
    print("--- Pandas Series Demo ---")
    data = [100, 200, 300, 400]
    labels = ['Jan', 'Feb', 'Mar', 'Apr']
    
    series = pd.Series(data, index=labels)
    print(f"Series with labels:\n{series}")
    print(f"Access by label 'Mar': {series['Mar']}")
    print("-" * 40)

def demo_pandas_dataframe():
    print("--- Pandas DataFrame Demo ---")
    data = {
        'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
        'Price': [1200, 25, 300, 75],
        'Stock': [15, 100, 45, 60]
    }
    
    df = pd.DataFrame(data)
    print(f"DataFrame:\n{df}")
    
    # Column Operations
    df['Total_Value'] = df['Price'] * df['Stock']
    print(f"\nDataFrame with calculated column:\n{df}")
    
    # Filtering
    expensive_products = df[df['Price'] > 100]
    print(f"\nProducts > $100:\n{expensive_products}")
    
    # Indexing (loc/iloc)
    print(f"\nFirst Row (iloc):\n{df.iloc[0]}")
    print("-" * 40)

def demo_data_cleaning():
    print("--- Data Cleaning Demo ---")
    raw_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice', None],
        'Age': [25, 30, np.nan, 25, 40],
        'Score': [85, 90, 95, 85, 70]
    }
    
    df = pd.DataFrame(raw_data)
    print(f"Original Data with Issues:\n{df}")
    
    # Handle Missing Values
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df = df.dropna(subset=['Name'])
    
    # Remove Duplicates
    df = df.drop_duplicates()
    
    print(f"\nCleaned Data:\n{df}")
    print("-" * 40)

if __name__ == "__main__":
    demo_pandas_series()
    demo_pandas_dataframe()
    demo_data_cleaning()
