from django import forms
from .models import Sales, Purchase


class BillingForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ('patient', 'item', 'quantity')


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('medicine_name',)
