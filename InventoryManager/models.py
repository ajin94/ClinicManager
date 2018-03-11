from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from PatientLedger.models import Patient


class MedicalCompany(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Branding(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Purchase(models.Model):
    medicine_name = models.CharField(max_length=250, null=False, blank=False)
    company_name = models.ForeignKey(MedicalCompany, null=True, blank=True, on_delete=models.DO_NOTHING)
    brand_name = models.ForeignKey(Branding, null=True, blank=True, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    expiry_date = models.DateField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Sales(models.Model):
    def validate_quantity(self):
        item_quantity = int(Purchase.objects.get(id=self.item).quantity)
        if self.quantity > item_quantity:
            raise ValidationError(
                _("Quantity exceeded stock"),
                params={'expiry_date', self.date}
            )

    patient = models.ForeignKey(Patient, blank=False, null=True, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Purchase, null=False, blank=False, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False, validators=[validate_quantity])
    unit_price = models.PositiveIntegerField(null=False, blank=False, editable=False)
    total_price = models.PositiveIntegerField(null=False, blank=False, editable=False)
    sale_date = models.DateField(auto_now_add=True)
