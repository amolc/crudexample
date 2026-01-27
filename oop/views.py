from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Person, Dog, Cat, BankAccount, UPIPayment, CardPayment, Book, FileLogger, DBLogger

# Classes and Objects
def create_person(request):
    p = Person(name="Amol", age=30)
    greeting = p.greet()
    return JsonResponse({"greeting": greeting})

# Inheritance and Polymorphism
def animal_sounds(request):
    d = Dog(name="Buddy", breed="Golden Retriever")
    c = Cat(name="Whiskers", color="Black")
    animals = [d, c]
    
    # Better example: getting specific details using polymorphism
    animal_info = [animal.speak() for animal in animals]
    
    return JsonResponse({
        "all_animal_info": animal_info,
        "dog_details": {
            "name": d.name,
            "breed": d.breed,
            "sound": d.speak()
        },
        "cat_details": {
            "name": c.name,
            "color": c.color,
            "sound": c.speak()
        }
    })


def bank_operations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        account = BankAccount.objects.create(account_holder=data['holder'])
        account.deposit(data.get('deposit', 0))
        balance = account.balance
        return JsonResponse({"balance": str(balance)})
    return JsonResponse({"error": "POST required"})

# Abstraction
def payments(request):
    upi = UPIPayment(upi_id="user@upi")
    card = CardPayment(card_number="1234567890123456")
    payments_list = [upi.pay(100), card.pay(200)]
    return JsonResponse({"payments": payments_list})

# Magic Methods
def book_operations(request):
    book1 = Book(title="Python Guide", pages=300)
    book2 = Book(title="Django Book", pages=400)
    total_pages = book1 + book2
    return JsonResponse({"total_pages": total_pages})

# Duck Typing
def logging_demo(request):
    loggers = [FileLogger(), DBLogger()]
    messages = []
    for logger in loggers:
        logger.log("Test message")
        messages.append(f"Logged with {type(logger).__name__}")
    return JsonResponse({"logs": messages})

# Error Handling
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
