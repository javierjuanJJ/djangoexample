from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price',]


class RawProductForm(forms.Form):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={
        "placeholder":"Your title"
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your description",
        "class":"new-class-name two",
        "rows": 16,
        "cols": 120,
        "id":"my-id-for-text-area"
    }))
    price = forms.DecimalField(initial=199.99)