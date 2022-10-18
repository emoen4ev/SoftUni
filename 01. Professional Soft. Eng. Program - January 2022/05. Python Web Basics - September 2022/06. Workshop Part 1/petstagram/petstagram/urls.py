from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

'''
After 'startapp APP_NAME':

1. Create 'APP_NAME/urls.py.
'''