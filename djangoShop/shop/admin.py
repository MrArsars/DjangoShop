from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from shop.models import CustomUser


# Register your models here.

admin.site.register(CustomUser)
