from django import forms
from business.models import Business, Category


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