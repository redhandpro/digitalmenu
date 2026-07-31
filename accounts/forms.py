from django import forms
from business.models import Business, Category, Product


class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = [
            "name",
            "logo",
            "address",
            "phone",
        ]


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = [
            "name",
        ]


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "description",
            "price",
            "image",
        ]


class BusinessUpdateForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = [
            "name",
            "logo",
            "address",
            "phone",
        ]
        # accounts/models.py (یا menu/models.py)
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    business = models.ForeignKey('Business', on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)  # برای آیکون
    order = models.PositiveIntegerField(default=0)  # ترتیب نمایش
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Categories"
    
    def str(self):
        return f"{self.business.name} - {self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)