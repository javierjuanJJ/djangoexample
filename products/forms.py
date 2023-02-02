from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))

    emailField = forms.EmailField()

    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your description",
        "class": "new-class-name two",
        "rows": 16,
        "cols": 120,
        "id": "my-id-for-text-area"
    }))

    # class Meta:
    #     model = Product
    #     fields = ['name','description','price',]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" or "news" in title:
            raise forms.ValidationError("This is not valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not valid email")
        return email



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