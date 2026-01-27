from django.urls import path
from . import views

urlpatterns = [
    path('person/', views.create_person, name='create_person'),
    path('animals/', views.animal_sounds, name='animal_sounds'),
    path('bank/', views.bank_operations, name='bank_operations'),
    path('payments/', views.payments, name='payments'),
    path('books/', views.book_operations, name='book_operations'),
    path('logging/', views.logging_demo, name='logging_demo'),
    path('error/', views.ErrorHandlingView.as_view(), name='error_handling'),
]