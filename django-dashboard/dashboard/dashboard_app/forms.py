# dashboard_app/forms.py
from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']
