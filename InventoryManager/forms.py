from django import forms


class BillingForm(forms.Form):
    patient = forms.CharField(label="Patient Name", max_length=250)