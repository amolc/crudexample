from django.db import models

# Classes and Objects
# A class is a blueprint, and an object is an instance of that class.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def greet(self):
        return f"Hello, my name is {self.name}"

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

# Inheritance
# Inheritance allows a class to acquire properties and behavior from a parent class.
class Animal(models.Model):
    name = models.CharField(max_length=100)

    def speak(self):
        return "Animal speaks"

    class Meta:
        abstract = True  # Making it abstract since we don't want a table for Animal

class Dog(Animal):
    breed = models.CharField(max_length=100)

    def speak(self):
        return "Dog barks"

class Cat(Animal):
    color = models.CharField(max_length=100)

    def speak(self):
        return "Cat meows"

# Polymorphism – Method Overriding
# Same method name, different behavior at runtime.
# Already shown in Dog and Cat overriding speak

# Encapsulation
# Encapsulation restricts direct access to internal data.
class BankAccount(models.Model):
    account_holder = models.CharField(max_length=100)
    _balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Private field

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

# Abstraction (Abstract Classes)
# Abstraction hides implementation details using abstract classes.
class Payment(models.Model):
    class Meta:
        abstract = True

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay method")

class UPIPayment(Payment):
    upi_id = models.CharField(max_length=100)

    def pay(self, amount):
        return f"Paid {amount} via UPI to {self.upi_id}"

    def __str__(self):
        return f"UPI Payment: {self.upi_id}"

class CardPayment(Payment):
    card_number = models.CharField(max_length=16)

    def pay(self, amount):
        return f"Paid {amount} via Card ending with {self.card_number[-4:]}"

    def __str__(self):
        return f"Card Payment: ****{self.card_number[-4:]}"

# Magic Methods
# Magic methods customize how objects behave with operators.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return f"Book: {self.title} with {self.pages} pages"

    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

# For Duck Typing, we can have loggers in views
class FileLogger:
    def log(self, message):
        print(f"Logging to file: {message}")

class DBLogger:
    def log(self, message):
        print(f"Logging to database: {message}")
