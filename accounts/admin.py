# accounts/admin.py
from django.contrib import admin
from .models import Business, Category, Product


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'owner', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'owner__username')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'business', 'order', 'is_active')
    list_filter = ('is_active', 'business')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_filter = ('available', 'category')
    search_fields = ('name',)