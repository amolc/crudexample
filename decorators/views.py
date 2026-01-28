from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.cache import cache_page, never_cache
from django.views.decorators.gzip import gzip_page
from datetime import datetime, timedelta
import re
import time
import functools

# --- Module 1: Decorators Demo ---
def performance_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        return result, duration
    return wrapper

@performance_logger
def heavy_computation():
    # Simulate work
    time.sleep(0.1)
    return "Computation Complete"

def decorator_demo_view(request):
    result, duration = heavy_computation()
    return JsonResponse({
        "concept": "Decorators",
        "action": "Performance Logging",
        "result": result,
        "execution_time_seconds": f"{duration:.4f}",
        "explanation": "This view uses a @performance_logger decorator to measure how long a function takes."
    })

# --- Module 1: Generators Demo ---
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def generator_demo_view(request):
    limit = int(request.GET.get('limit', 10))
    sequence = list(fibonacci_gen(limit))
    return JsonResponse({
        "concept": "Generators",
        "action": "Fibonacci Sequence",
        "limit": limit,
        "sequence": sequence,
        "explanation": "Generators use 'yield' to produce values lazily, saving memory."
    })

# --- Module 3: Regex Demo ---
def regex_demo_view(request):
    text = request.GET.get('text', 'My email is amol@example.com and phone is 123-456-7890')
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    
    return JsonResponse({
        "concept": "Regular Expressions",
        "input_text": text,
        "extracted_emails": emails,
        "extracted_phones": phones,
        "explanation": "Regex allows for powerful pattern matching and data extraction from strings."
    })

# --- Module 4: Datetime Demo ---
def datetime_demo_view(request):
    now = datetime.now()
    future_date = now + timedelta(days=30)
    
    return JsonResponse({
        "concept": "Datetime Operations",
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "future_date_30_days": future_date.strftime("%Y-%m-%d"),
        "day_of_week": now.strftime("%A"),
        "explanation": "Python's datetime module handles parsing, formatting, and date arithmetic easily."
    })

# --- Django Decorators Demos (from django-readme.md) ---

@login_required
def dashboard_view(request):
    return JsonResponse({
        "status": "success",
        "message": "Welcome to the Dashboard!",
        "user": request.user.username,
        "decorator": "@login_required"
    })

@staff_member_required
def admin_panel_view(request):
    return JsonResponse({
        "status": "success",
        "message": "Welcome to the Staff Admin Panel!",
        "user": request.user.username,
        "is_staff": request.user.is_staff,
        "decorator": "@staff_member_required"
    })

@require_GET
def get_only_view(request):
    return JsonResponse({
        "message": "This view only accepts GET requests.",
        "decorator": "@require_GET"
    })

@require_POST
@csrf_exempt # Exempting for easy testing via tool/curl
def post_only_view(request):
    return JsonResponse({
        "message": "This view only accepts POST requests.",
        "decorator": "@require_POST"
    })

@cache_page(60 * 15)
def cached_view(request):
    return JsonResponse({
        "message": "This response is cached for 15 minutes.",
        "server_time": datetime.now().strftime("%H:%M:%S"),
        "decorator": "@cache_page"
    })

@gzip_page
def large_data_view(request):
    # Simulate a large response
    data = "Python is great! " * 1000
    return HttpResponse(f"Gzipped response demo. Data length: {len(data)}")
