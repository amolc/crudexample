from django.urls import path
from . import views

urlpatterns = [
    path('ref-count/', views.ref_count_demo, name='ref_count_demo'),
    path('gc-status/', views.gc_status_demo, name='gc_status_demo'),
    path('optimization/', views.memory_optimization_demo, name='memory_optimization_demo'),
    path('cyclic-refs/', views.cyclic_reference_demo, name='cyclic_reference_demo'),
]
