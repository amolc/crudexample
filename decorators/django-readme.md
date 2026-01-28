# 🧩 Django Decorators – Complete Guide (With Examples)

This document explains **Django decorators** with practical, runnable examples. It covers decorators used in **function-based views (FBVs)** and **class-based views (CBVs)**.

---

## 🎯 Objectives

* Understand why decorators are used in Django
* Apply built-in Django decorators correctly
* Secure, optimize, and control Django views
* Write and apply custom decorators

---

## 🧠 Prerequisites

* Python functions and decorators
* Basic Django project knowledge
* Understanding of Django views

---

## 🔐 Authentication & Authorization Decorators

### `login_required`

Ensures only authenticated users can access a view.

```python
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashboard(request):
    return HttpResponse("Welcome to Dashboard")
```

---

### `permission_required`

Checks whether a user has a specific permission.

```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.view_employee', raise_exception=True)
def employee_view(request):
    return HttpResponse("Employee Details")
```

---

### `user_passes_test`

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

### `staff_member_required`

Restricts access to Django staff users.

```python
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_panel(request):
    return HttpResponse("Admin Panel")
```

---

## 🌐 HTTP Method Restriction Decorators

### `require_GET`

```python
from django.views.decorators.http import require_GET

@require_GET
def get_data(request):
    return HttpResponse("GET request only")
```

---

### `require_POST`

```python
from django.views.decorators.http import require_POST

@require_POST
def submit_form(request):
    return HttpResponse("POST request only")
```

---

### `require_http_methods`

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def mixed_view(request):
    return HttpResponse("GET or POST allowed")
```

---

## 🛡️ CSRF Protection Decorators

### `csrf_protect`

```python
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def secure_form(request):
    return HttpResponse("CSRF protected view")
```

---

### `csrf_exempt`

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    return HttpResponse("Webhook received")
```

---

## 🚀 Performance & Caching Decorators

### `cache_page`

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def home(request):
    return HttpResponse("Cached Home Page")
```

---

### `never_cache`

```python
from django.views.decorators.cache import never_cache

@never_cache
def sensitive_view(request):
    return HttpResponse("No caching allowed")
```

---

### `gzip_page`

```python
from django.views.decorators.gzip import gzip_page

@gzip_page
def large_response(request):
    return HttpResponse("Large response data")
```

---

## 🔁 Conditional & Cache-Control Decorators

### `condition`

```python
from django.views.decorators.http import condition
from django.utils import timezone

def last_modified(request, *args, **kwargs):
    return timezone.now()

@condition(last_modified_func=last_modified)
def conditional_view(request):
    return HttpResponse("Conditional response")
```

---

### `vary_on_headers`

```python
from django.views.decorators.vary import vary_on_headers

@vary_on_headers('User-Agent')
def device_specific_view(request):
    return HttpResponse("Varies by device")
```

---

### `vary_on_cookie`

```python
from django.views.decorators.vary import vary_on_cookie

@vary_on_cookie
def cookie_based_view(request):
    return HttpResponse("Varies by cookie")
```

---

## 🔒 Security Decorators

### `sensitive_post_parameters`

```python
from django.views.decorators.debug import sensitive_post_parameters

@sensitive_post_parameters('password', 'credit_card')
def payment_view(request):
    return HttpResponse("Secure payment")
```

---

### Clickjacking Protection

```python
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
def no_iframe_view(request):
    return HttpResponse("Iframes not allowed")
```

---

## 🧱 Class-Based Views (CBV) Decorator Usage

### `method_decorator`

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

* Use decorators for cross-cutting concerns
* Avoid excessive stacking of decorators
* Use `csrf_exempt` sparingly
* Prefer `method_decorator` for CBVs

---

Happy Coding with Django 🚀
