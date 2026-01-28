from django.urls import path
from . import views

urlpatterns = [
    # Python Intermediate Demos
    path('decorators-demo/', views.decorator_demo_view, name='decorators_demo'),
    path('generators-demo/', views.generator_demo_view, name='generators_demo'),
    path('regex-demo/', views.regex_demo_view, name='regex_demo'),
    path('datetime-demo/', views.datetime_demo_view, name='datetime_demo'),
    
    # Django Decorator Demos
    path('django/dashboard/', views.dashboard_view, name='django_dashboard'),
    path('django/admin-panel/', views.admin_panel_view, name='django_admin_panel'),
    path('django/get-only/', views.get_only_view, name='django_get_only'),
    path('django/post-only/', views.post_only_view, name='django_post_only'),
    path('django/cached/', views.cached_view, name='django_cached'),
    path('django/large-data/', views.large_data_view, name='django_large_data'),
]
