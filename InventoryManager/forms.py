from django import forms
from .models import Sales


class BillingForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ('patient', 'item')
