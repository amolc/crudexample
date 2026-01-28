# 📘 Python Intermediate Concepts – Course Material

## Module 1: Decorators & Generators

### 🎯 Learning Objectives
- Understand function wrapping and lazy evaluation
- Write reusable, clean, and optimized Python code

### 🔹 Decorators
#### What is a Decorator?
A decorator is a function that modifies another function’s behavior without changing its source code.

#### Why use decorators?
- Logging
- Authentication & authorization
- Performance monitoring
- Input validation

#### Basic Decorator Example
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

#### Decorators with Arguments
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

#### Common Built-in Decorators
- `@staticmethod`
- `@classmethod`
- `@property`

---

### 🔹 Generators
#### What is a Generator?
A generator is a function that returns values one at a time using `yield`.

#### Why Generators?
- Memory efficient
- Ideal for large datasets
- Lazy execution

#### Generator Example
```python
def count_up(n):
    for i in range(n):
        yield i

for num in count_up(5):
    print(num)
```

#### Generator vs List
| Feature | List | Generator |
| :--- | :--- | :--- |
| **Memory** | High | Low |
| **Execution** | Immediate | Lazy |
| **Use Case** | Small data | Large streams |

#### 🧪 Practice Tasks
1. Create a decorator to measure execution time
2. Write a generator for Fibonacci numbers

---

## Module 2: File Handling & I/O Operations

### 🎯 Learning Objectives
- Read, write, and manage files safely
- Understand file modes and contexts

### 🔹 File Modes
| Mode | Description |
| :--- | :--- |
| `r` | Read |
| `w` | Write (overwrite) |
| `a` | Append |
| `rb` | Read binary |
| `wb` | Write binary |

### 🔹 Reading Files
```python
with open("data.txt", "r") as f:
    content = f.read()
```

### 🔹 Writing Files
```python
with open("data.txt", "w") as f:
    f.write("Hello Python")
```

### 🔹 Reading Line by Line
```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

### 🔹 Handling Exceptions
```python
try:
    with open("file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

#### 🧪 Practice Tasks
1. Read a CSV file and count records
2. Append logs with timestamps

---

## Module 3: Regular Expressions (Regex)

### 🎯 Learning Objectives
- Perform pattern matching and text validation
- Extract and clean unstructured data

### 🔹 What is Regex?
Regex is a pattern-matching language used for searching and manipulating text.

### 🔹 Common Patterns
| Pattern | Meaning |
| :--- | :--- |
| `.` | Any character |
| `\d` | Digit |
| `\w` | Word character |
| `+` | One or more |
| `*` | Zero or more |
| `^` | Start |
| `$` | End |

### 🔹 Regex Example
```python
import re

text = "Email: test@example.com"
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group())
```

### 🔹 Common Regex Functions
- `re.search()`
- `re.findall()`
- `re.sub()`
- `re.match()`

#### 🧪 Practice Tasks
1. Validate phone numbers
2. Extract emails from text files

---

## Module 4: Working with Dates & Times

### 🎯 Learning Objectives
- Handle timestamps, time differences, and formatting
- Work with real-world date/time problems

### 🔹 datetime Module
```python
from datetime import datetime
now = datetime.now()
print(now)
```

### 🔹 Formatting Dates
```python
now.strftime("%d-%m-%Y %H:%M:%S")
```

### 🔹 Parsing Dates
```python
datetime.strptime("25-01-2026", "%d-%m-%Y")
```

### 🔹 Date Arithmetic
```python
from datetime import timedelta
future = now + timedelta(days=10)
```

#### 🧪 Practice Tasks
1. Calculate age from DOB
2. Find difference between two timestamps

---

## Module 5: Python Package Management (pip)

### 🎯 Learning Objectives
- Install, manage, and freeze dependencies
