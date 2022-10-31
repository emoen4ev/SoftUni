from django.contrib import admin

from CarCollection.CarCollectionWeb.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass