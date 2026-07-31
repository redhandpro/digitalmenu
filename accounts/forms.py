در# accounts/forms.py
from django import forms
from .models import Business, Category, Product  # فقط مدل‌ها را import کنید

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'address', 'phone', 'logo']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # این مدل از models.py می‌آید
        fields = ['name', 'description', 'icon', 'order', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثلاً: 🍔'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'available']