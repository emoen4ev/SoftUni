
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("templates_demos.web.urls"))
]

'''
1. Create new django app(named 'web') to root templates_demos folder
2. Move new django app('web') to templates_demos\templates_demos folder
3. Add 'web' app to INSTALLED_APPS in settings.py.
4. Create urls.py in the new 'web' app
5. Include app's urls.py in project's urls.py

'''