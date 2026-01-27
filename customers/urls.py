from django.urls import path
from .views import CustomerAPIView,CustomerEdit,CustomerDelete,CustomerLogin

urlpatterns = [
    path('', CustomerAPIView.as_view()),
    path('edit/<int:id>/', CustomerEdit.as_view()),
    path('delete/<int:id>/', CustomerDelete.as_view()),
    path('login/', CustomerLogin.as_view()),
]