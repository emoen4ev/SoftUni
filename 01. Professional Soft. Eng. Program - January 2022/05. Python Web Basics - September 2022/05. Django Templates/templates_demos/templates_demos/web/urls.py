from django.urls import path

from templates_demos.web.views import index

urlpatterns = (
    path('', index, name= 'index'),

)