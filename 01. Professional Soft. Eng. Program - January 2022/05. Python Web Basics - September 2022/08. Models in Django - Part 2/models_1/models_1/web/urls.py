from django.urls import path

from models_1.web.views import index, delete_employee

urlpatterns = (
    path('', index, name='index'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
)