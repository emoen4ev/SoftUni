from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('petstagram.accounts.urls')),
]

'''
After 'startapp APP_NAME':

1. Create 'APP_NAME/urls.py with empty 'urlpatterns'(urlpatterns = (), list or tuple).
2. Include 'APP_NAME/urls.py' into project's urls.py.
3. Add 'APP_NAME' to 'INSTALLED_APPS' in settings.py.

'''