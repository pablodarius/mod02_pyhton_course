from django import forms
from .models import History_Carts

class CartForm(forms.Form):
    asunto = forms.CharField()
