from django.contrib import admin
from .models import Business, Category, Product


admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Product)