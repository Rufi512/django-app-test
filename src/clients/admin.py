from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

# Register your models here.

class CustomerChoice(admin.ModelAdmin):
	search_field = ('username'),
	ordering = ['username']


admin.site.register(Customer,CustomerChoice)

