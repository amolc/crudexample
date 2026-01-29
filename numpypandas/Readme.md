# � Numerical & Data Computing with NumPy and Pandas

This course covers high-performance numerical computing and data manipulation using the industry-standard libraries: **NumPy** and **Pandas**.

---

## 🎯 Course Objectives
- Perform high-performance numerical computing using **NumPy**.
- Manipulate, analyze, and clean real-world datasets using **Pandas**.
- Work confidently with **Series** & **DataFrames**.
- Build a strong foundation for **Data Science, ML, FinTech & AI**.

---

## 🧭 Course Flow
1. **NumPy** → Numerical & matrix foundation
2. **Pandas Series** → Labeled 1D data
3. **Pandas DataFrame** → Real datasets (CSV, Excel, DB extracts)
4. **Applied Analysis** → Business & ML readiness

---

## 🧩 Module-Wise Structure

### 🟦 MODULE 1: Introduction
- What is Numerical Computing?
- NumPy vs Python Lists
- **Example:**
```python
import numpy as np
import time

# List performance
size = 1000000
l1, l2 = range(size), range(size)
start = time.time()
result = [x + y for x, y in zip(l1, l2)]
print(f"List time: {time.time() - start:.4f}s")

# NumPy performance
a1, a2 = np.arange(size), np.arange(size)
start = time.time()
result = a1 + a2
print(f"NumPy time: {time.time() - start:.4f}s")
```

### 🟦 MODULE 2: NumPy Fundamentals
- ndarray basics, dtypes, shape, and dimensions.
- **Example:**
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Shape: {arr.shape}, Dtype: {arr.dtype}, Dimensions: {arr.ndim}")
```

### 🟦 MODULE 3: Operations & Broadcasting
- Vectorization and broadcasting rules.
- **Example:**
```python
a = np.array([1, 2, 3])
b = 2
print(f"Broadcasting: {a * b}") # [2, 4, 6]
```

### 🟦 MODULE 4: Indexing & Slicing
- Boolean masking and fancy indexing.
- **Example:**
```python
arr = np.array([1, 5, 10, 15])
print(f"Filtered: {arr[arr > 8]}") # [10, 15]
```

### 🟦 MODULE 5: Matrix Operations
- Dot products, transpose, and inverse.
- **Example:**
```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(f"Matrix Product:\n{np.dot(m1, m2)}")
```

---

### � MODULE 8: Transition to Pandas
- NumPy Array → Pandas Series.
- **Example:**
```python
import pandas as pd
data = np.array([10, 20, 30])
series = pd.Series(data, index=['a', 'b', 'c'])
print(series['b']) # 20
```

### 🟩 MODULE 9: Pandas DataFrame Fundamentals
- Creation, indexing (`loc`, `iloc`), and column operations.
- **Example:**
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})
print(df.iloc[0]) # First row
```

### 🟩 MODULE 10: Data Cleaning
- Handling missing values (`dropna`, `fillna`) and duplicates.
- **Example:**
```python
df = pd.DataFrame({'A': [1, np.nan, 3]})
df_cleaned = df.fillna(0)
print(df_cleaned)
```

### 🟩 MODULE 11: Data Analysis & Aggregation
- GroupBy and aggregations.
- **Example:**
```python
df = pd.DataFrame({
    'Dept': ['Sales', 'IT', 'Sales'],
    'Rev': [100, 200, 150]
})
print(df.groupby('Dept').sum())
```

### 🟩 MODULE 12: File Handling
- CSV, Excel, and JSON operations.
- **Example:**
```python
# df = pd.read_csv('data.csv')
# df.to_excel('output.xlsx', index=False)
```

---

## 🟪 Real-World Applications
- Data Science pipelines
- ML preprocessing
- FinTech & trading analytics
- Business dashboards

---

Happy Computing with NumPy & Pandas 🚀
