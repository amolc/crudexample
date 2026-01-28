# 🚀 Django CRUD & OOP Demo Endpoints

This document provides a comprehensive list of all available endpoints in the project, categorized by their functionality. Use these to demo the features of the application.

---

## 👥 Customer Management (`/customers/`)
*Base URL: `/customers/`*

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | List all customers in the database. |
| `/` | `POST` | Create a new customer. Requires `name`, `email`, `phone`, `address`, `username`, `password`. |
| `/edit/<id>/` | `GET` | Retrieve customer details for editing. |
| `/delete/<id>/` | `GET` | Delete a customer by ID. |
| `/login/` | `POST` | Login endpoint. Requires `username` and `password`. Returns 401 if invalid. |

---

## 🏗️ Object-Oriented Programming Demos (`/oop/`)
*Base URL: `/oop/`*

| Endpoint | Description | Key OOP Concept |
| :--- | :--- | :--- |
| `/person/` | Person and Employee hierarchy. | **Inheritance** |
| `/animals/` | Animal, Dog, and Cat sounds with detailed attributes. | **Polymorphism** |
| `/bank/` | Private balances and secure deposits/withdrawals. | **Encapsulation** |
| `/payments/` | CreditCard and PayPal implementations. | **Abstraction** |
| `/books/` | Handling different ways to initialize/display books. | **Method Overloading** |
| `/logging/` | Multiple parent classes (Logger, Database). | **Multiple Inheritance** |
| `/error/` | Custom exceptions and graceful failure. | **Exception Handling** |

---

## 🧠 Python & Django Concepts (`/concepts/`)
*Base URL: `/concepts/`*

### **Python Intermediate**
| Endpoint | Description |
| :--- | :--- |
| `/decorators-demo/` | Demonstrates function wrapping and timing decorators. |
| `/generators-demo/` | Demonstrates lazy evaluation and memory efficiency. |
| `/regex-demo/` | Demonstrates pattern matching for emails and phones. |
| `/datetime-demo/` | Demonstrates formatting and time arithmetic. |

### **Django Built-in Decorators**
| Endpoint | Method | Required Decorator |
| :--- | :--- | :--- |
| `/django/dashboard/` | `GET` | `@login_required` (Redirects to login if not authenticated) |
| `/django/admin-panel/` | `GET` | `@staff_member_required` (Requires admin status) |
| `/django/get-only/` | `GET` | `@require_GET` (Returns 405 if POSTed) |
| `/django/post-only/` | `POST` | `@require_POST` (Returns 405 if GETed) |
| `/django/cached/` | `GET` | `@cache_page(15 min)` (Demonstrates server-side caching) |
| `/django/large-data/` | `GET` | `@gzip_page` (Compresses large JSON responses) |

---

## 🛠️ Quick Demo Commands

### **1. Test Login**
```bash
curl -X POST http://localhost:8000/customers/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpassword"}'
```

### **2. Test Animal Sounds (Polymorphism)**
```bash
curl http://localhost:8000/oop/animals/
```

### **3. Test GET Only Restriction**
```bash
# This will succeed
curl -X GET http://localhost:8000/concepts/django/get-only/

# This will fail (405 Method Not Allowed)
curl -X POST http://localhost:8000/concepts/django/get-only/
```

### **4. Test Data Compression**
```bash
curl -I -H "Accept-Encoding: gzip" http://localhost:8000/concepts/django/large-data/
# Look for 'Content-Encoding: gzip' in the headers
```

---

## 🔑 Admin Access
- **URL**: `http://localhost:8000/admin/`
- **Credentials**: Use your superuser account to manage customers and view logs.
