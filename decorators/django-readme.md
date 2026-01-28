# 🎯 Django Decorators – Complete Guide (With Examples)

This document explains **Django decorators** with practical, runnable examples. It covers decorators used in **function-based views (FBVs)** and **class-based views (CBVs)**.

### 🔹 Quick Reference Table

| Category | Decorators |
| :--- | :--- |
| **🔐 Auth** | `login_required`, `permission_required`, `staff_member_required` |
| **🌐 HTTP** | `require_GET`, `require_POST`, `require_http_methods` |
| **🛡️ CSRF** | `csrf_protect`, `csrf_exempt` |
| **🚀 Cache** | `cache_page`, `never_cache` |
| **🔒 Security** | `sensitive_post_parameters`, `xframe_options_*` |
| **📈 Performance** | `gzip_page`, `condition` |
| **🧱 CBV** | `method_decorator` |

---

## 🎯 Learning Objectives
- Understand why decorators are used in Django
- Apply built-in Django decorators correctly
- Secure, optimize, and control Django views
- Write and apply custom decorators

---

## 🧠 Prerequisites
- Python functions and decorators
- Basic Django project knowledge
- Understanding of Django views

---

## 🔐 Authentication & Authorization
### 🔹 `login_required`
Ensures only authenticated users can access a view.

```python
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashboard(request):
    return HttpResponse("Welcome to Dashboard")
```

---

### 🔹 `permission_required`
Checks whether a user has a specific permission.

```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.view_employee', raise_exception=True)
def employee_view(request):
    return HttpResponse("Employee Details")
```

---

### 🔹 `user_passes_test`
Applies custom user validation logic.

```python
from django.contrib.auth.decorators import user_passes_test

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

@user_passes_test(is_manager)
def manager_dashboard(request):
    return HttpResponse("Manager Area")
```

---

### 🔹 `staff_member_required`
Restricts access to Django staff users.

```python
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_panel(request):
    return HttpResponse("Admin Panel")
```

---

## 🌐 HTTP Method Restrictions
### 🔹 `require_GET`
```python
from django.views.decorators.http import require_GET

@require_GET
def get_data(request):
    return HttpResponse("GET request only")
```

---

### 🔹 `require_POST`
```python
from django.views.decorators.http import require_POST

@require_POST
def submit_form(request):
    return HttpResponse("POST request only")
```

---

### 🔹 `require_http_methods`
```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def mixed_view(request):
    return HttpResponse("GET or POST allowed")
```

---

## 🛡️ CSRF Protection
### 🔹 `csrf_protect`
```python
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def secure_form(request):
    return HttpResponse("CSRF protected view")
```

---

### 🔹 `csrf_exempt`
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    return HttpResponse("Webhook received")
```

---

## 🚀 Performance & Caching
### 🔹 `cache_page`
```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def home(request):
    return HttpResponse("Cached Home Page")
```

---

### 🔹 `never_cache`
```python
from django.views.decorators.cache import never_cache

@never_cache
def sensitive_view(request):
    return HttpResponse("No caching allowed")
```

---

### 🔹 `gzip_page`
```python
from django.views.decorators.gzip import gzip_page

@gzip_page
def large_response(request):
    return HttpResponse("Large response data")
```

---

## � Security & Headers
### � `sensitive_post_parameters`
```python
from django.views.decorators.debug import sensitive_post_parameters

@sensitive_post_parameters('password', 'credit_card')
def payment_view(request):
    return HttpResponse("Secure payment")
```

---

### 🔹 Clickjacking Protection
```python
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
def no_iframe_view(request):
    return HttpResponse("Iframes not allowed")
```

---

## 🧱 Class-Based Views (CBV)
### 🔹 `method_decorator`
```python
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return HttpResponse("User Profile")
```

---

## 🛠️ Custom Decorator Example
```python
from django.http import HttpResponseForbidden

def ajax_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return HttpResponseForbidden("AJAX requests only")
        return view_func(request, *args, **kwargs)
    return wrapper

@ajax_required
def ajax_view(request):
    return HttpResponse("AJAX request successful")
```

---

## ✅ Best Practices
- Use decorators for cross-cutting concerns (Auth, Logging, Caching)
- Avoid excessive stacking of decorators to keep views readable
- Use `csrf_exempt` sparingly and only when absolutely necessary
- Prefer `method_decorator` for CBVs to maintain clean class definitions

---

Happy Coding with Django 🚀

