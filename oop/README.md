# OOP Concepts Demonstration

This Django app demonstrates fundamental Object-Oriented Programming (OOP) concepts using Django models and views. Each concept is implemented with practical examples that you can test via API endpoints.

## Overview

The app includes models and views that showcase:
- Classes and Objects
- Inheritance
- Polymorphism (Method Overriding)
- Encapsulation
- Abstraction
- Magic Methods
- Duck Typing
- Error Handling and Exceptions

## Setup

1. Ensure the `oop` app is added to `INSTALLED_APPS` in `settings.py`
2. Run migrations: `python manage.py makemigrations oop && python manage.py migrate`
3. Start the server: `python manage.py runserver`
4. Access endpoints at `http://localhost:8000/oop/`

## OOP Concepts Explained

### 1. Classes and Objects

A class is a blueprint for creating objects. An object is an instance of a class.

**Model Example:**
```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def greet(self):
        return f"Hello, my name is {self.name}"

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"
```

**Test it:**
```
GET /oop/person/
```
Creates a Person object and returns the greeting.

### 2. Inheritance

Inheritance allows a class to inherit properties and methods from a parent class.

**Model Example:**
```python
class Animal(models.Model):
    name = models.CharField(max_length=100)

    def speak(self):
        return "Animal speaks"

    class Meta:
        abstract = True

class Dog(Animal):
    breed = models.CharField(max_length=100)

    def speak(self):
        return "Dog barks"

class Cat(Animal):
    color = models.CharField(max_length=100)

    def speak(self):
        return "Cat meows"
```

**Test it:**
```
GET /oop/animals/
```
Shows how Dog and Cat inherit from Animal but override the speak method.

### 3. Polymorphism - Method Overriding

Same method name, different behavior at runtime based on the object type.

**Demonstrated in:** Dog and Cat classes above.

The `speak()` method behaves differently for Dog and Cat objects, even though they share the same method name.

### 4. Encapsulation

Encapsulation restricts direct access to internal data, providing controlled access through methods.

**Model Example:**
```python
class BankAccount(models.Model):
    account_holder = models.CharField(max_length=100)
    _balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.save()
        else:
            raise ValueError("Invalid withdrawal amount")

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"Account of {self.account_holder}: ${self.balance}"
```

**Test it:**
```
POST /oop/bank/
Content-Type: application/json
{
    "holder": "John Doe",
    "deposit": 100.50
}
```
Creates an account and deposits money, demonstrating encapsulated balance management.

### 5. Abstraction

Abstraction hides implementation details and shows only essential features.

**Model Example:**
```python
class Payment(models.Model):
    class Meta:
        abstract = True

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay method")

class UPIPayment(Payment):
    upi_id = models.CharField(max_length=100)

    def pay(self, amount):
        return f"Paid {amount} via UPI to {self.upi_id}"

class CardPayment(Payment):
    card_number = models.CharField(max_length=16)

    def pay(self, amount):
        return f"Paid {amount} via Card ending with {self.card_number[-4:]}"
```

**Test it:**
```
GET /oop/payments/
```
Shows different payment implementations without exposing internal details.

### 6. Magic Methods

Magic methods customize how objects behave with built-in operations.

**Model Example:**
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return f"Book: {self.title} with {self.pages} pages"

    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented
```

**Test it:**
```
GET /oop/books/
```
Demonstrates custom string representation and operator overloading (adding page counts).

### 7. Duck Typing

Objects are interchangeable if they have the same methods, regardless of their class.

**View Example:**
```python
class FileLogger:
    def log(self, message):
        print(f"Logging to file: {message}")

class DBLogger:
    def log(self, message):
        print(f"Logging to database: {message}")

def write_log(logger):
    logger.log("Test message")
```

**Test it:**
```
GET /oop/logging/
```
Shows how FileLogger and DBLogger can be used interchangeably since both have a `log()` method.

### 8. Error Handling and Exceptions

Graceful handling of runtime errors using try/except blocks.

**View Example:**
```python
@method_decorator(csrf_exempt, name='dispatch')
class ErrorHandlingView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            x = int(data.get('number', '0'))
            result = 10 / x
            return JsonResponse({"result": result})
        except ZeroDivisionError:
            return JsonResponse({"error": "Cannot divide by zero"})
        except ValueError:
            return JsonResponse({"error": "Invalid input"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        finally:
            print("Execution complete")
```

**Test it:**
```
POST /oop/error/
Content-Type: application/json
{
    "number": "0"
}
```
Try different inputs to see various exception handling scenarios.

## API Endpoints Summary

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/oop/person/` | GET | Classes and Objects demo |
| `/oop/animals/` | GET | Inheritance & Polymorphism demo |
| `/oop/bank/` | POST | Encapsulation demo |
| `/oop/payments/` | GET | Abstraction demo |
| `/oop/books/` | GET | Magic Methods demo |
| `/oop/logging/` | GET | Duck Typing demo |
| `/oop/error/` | POST | Error Handling demo |

## Key Takeaways

- **Classes and Objects**: Blueprints and instances
- **Inheritance**: Code reuse through parent-child relationships
- **Polymorphism**: Same interface, different implementations
- **Encapsulation**: Data hiding and controlled access
- **Abstraction**: Hiding complexity, showing essentials
- **Magic Methods**: Customizing built-in operations
- **Duck Typing**: Interface-based compatibility
- **Error Handling**: Robust exception management

This app provides a comprehensive foundation for understanding OOP principles in a practical, Django-based context.