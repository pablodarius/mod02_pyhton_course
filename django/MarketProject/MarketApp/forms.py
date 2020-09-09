from django import forms
from .models import History_Carts

class CartForm(forms.ModelForm):
    
    class Meta:
        model = History_Carts
        fields = ('idCart', 'nameProduct', 'nameMarket', 'priceProduct',)