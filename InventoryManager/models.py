from PatientLedger.models import Patient
from django.db import models
from django.db.models.signals import pre_save


class MedicalCompany(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name


class Branding(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name


class MedicalRep(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    company_name = models.ForeignKey(MedicalCompany, null=False, blank=False, on_delete=models.DO_NOTHING)
    contact_number = models.CharField(max_length=13, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("name", "company_name")

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.company_name)


class Purchase(models.Model):
    medicine_name = models.CharField(max_length=250, null=False, blank=False)
    company_name = models.ForeignKey(MedicalCompany, null=False, blank=False, on_delete=models.DO_NOTHING)
    brand_name = models.ForeignKey(Branding, null=True, blank=True, on_delete=models.DO_NOTHING)
    representative_name = models.ForeignKey(MedicalRep, null=False, blank=False, on_delete=models.DO_NOTHING)
    unit_price = models.PositiveIntegerField(null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    expiry_date = models.DateField(null=False, blank=False)
    invoice_amount = models.PositiveIntegerField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.medicine_name


class Sales(models.Model):
    patient = models.ForeignKey(Patient, blank=False, null=True, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Purchase, null=False, blank=False, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    unit_price = models.PositiveIntegerField(null=False, blank=True, editable=False)
    total_price = models.PositiveIntegerField(null=False, blank=True, editable=False)
    sale_date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = "Sales"
