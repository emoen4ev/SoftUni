from django.urls import path

from models_1.web.views import index

urlpatterns = (
    path('', index, name='index'),
)