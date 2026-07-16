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
        from business.models import Product


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
        