from django import forms


class BillingForm(forms.Form):
    patient = forms.CharField(max_length=250)
    date = forms.DateField(auto_add=True)
