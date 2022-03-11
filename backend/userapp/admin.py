from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BackUser

admin.site.register(BackUser, UserAdmin)
