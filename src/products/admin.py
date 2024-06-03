from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Categories

admin.site.register(Product)
admin.site.register(Categories)