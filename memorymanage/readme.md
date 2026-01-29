# 🧠 Python Memory Management – Complete Course

This repository contains structured learning material, explanations, and hands-on examples covering **how Python manages memory internally** and how developers can write **memory-efficient, high-performance code**.

The course is designed to bridge the gap between *writing Python code* and *understanding what happens under the hood*.

---

## 📌 Course Overview

Python provides **automatic memory management**, which makes development easy—but understanding its internals helps you:

- Avoid memory leaks
- Optimize large applications
- Write scalable backend and data systems
- Perform better in interviews and system design discussions

This course explains **memory allocation, garbage collection, and optimization techniques** with practical examples.

---



## 🧩 Topics Covered

### 1️⃣ Automatic Memory Management
- What automatic memory management means
- Object creation and destruction
- How Python abstracts memory handling

#### 📍 Example:
```python
a = [1, 2, 3]
a = None  # memory becomes eligible for cleanup
```

---

### 2️⃣ Private Heap & Garbage Collection
- Python’s private heap architecture
- Role of the garbage collector
- Enabling and disabling GC

#### 📍 Example:
```python
import gc
print(f"Is GC enabled? {gc.isenabled()}")
```

---

### 3️⃣ Reference Counting
- How Python tracks object references
- Immediate memory deallocation
- Limitations of reference counting

#### 📍 Example:
```python
import sys

a = []
print(f"Initial ref count: {sys.getrefcount(a)}")

b = a
print(f"Ref count after 'b = a': {sys.getrefcount(a)}")

del b
print(f"Ref count after 'del b': {sys.getrefcount(a)}")
```

---

### 4️⃣ Generational Garbage Collection
- Why generations exist
- Generation 0, 1, and 2
- Collection thresholds and performance benefits

#### 📍 Example:
```python
import gc
print(f"GC Thresholds: {gc.get_threshold()}")
```

---

### 5️⃣ Cyclic References
- What cyclic references are
- Why reference counting fails
- How GC detects and cleans cycles

#### 📍 Example:
```python
class Node:
    def __init__(self):
        self.other = None

a = Node()
b = Node()

# Creating a cycle
a.other = b
b.other = a
```

---

### 6️⃣ Memory Allocation & Optimization Techniques
- **Generators vs Lists**: Lazy vs eager evaluation.
- **Using `__slots__`**: Reducing memory footprint of class instances.
- **Object reuse and caching**: Interning and pooling.
- **Explicit deletion**: Using `del`.
- **Weak references**: Using the `weakref` module.

#### 📍 Examples:

**Generator (memory efficient)**
```python
# Uses constant memory regardless of range size
nums = (i for i in range(10_000_000))
```

**Using `__slots__`**
```python
class User:
    __slots__ = ("id", "name")
    def __init__(self, id, name):
        self.id = id
        self.name = name
```

---

## ✅ Best Practices
- Prefer generators for large data processing.
- Use `__slots__` for classes with millions of instances.
- Be mindful of cyclic references in long-running processes.
- Profile memory usage using tools like `objgraph` or `memory_profiler`.

---

Happy Coding with Python 🚀
