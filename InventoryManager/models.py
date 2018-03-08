from django.db import models

# Create your models here.


class MedicalCompany(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Branding(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Purchase(models.Model):
    medicine_name = models.CharField(max_length=250, null=False, blank=False)
    company_name = models.ForeignKey(MedicalCompany, null=True, blank=True, on_delete=models.DO_NOTHING)
    brand_name = models.ForeignKey(Branding, null=True, blank=True, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Inventory(models.Model): pass


class Sales(models.Model): pass
