from django import forms
from .models import Sales, Purchase, MedicalRep


class DateInput(forms.DateInput):
    input_type = 'date'


class SalesBillingForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ('item', 'quantity',)


class PurchaseBillingForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('medicine_name', 'medical_rep', 'company_name', 'brand_name',
                  'unit_price', 'quantity', 'expiry_date')
        widgets = {
            'expiry_date': DateInput()
        }