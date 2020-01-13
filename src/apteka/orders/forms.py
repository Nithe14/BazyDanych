from django import forms

from .models import OrdersProducts

class OrderForm (forms.Form):
    product_id = forms.CharField()
    amount     = forms.IntegerField()
    