from PatientLedger.models import Patient
from django.db import models


# abbreviations of unique ID's used in the table
# SCSNO - stock number
# SCPID - purchase ID
# SCSID - saels ID

class MedicalCompany(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)
    address = models.CharField(max_length=500, unique=True, null=False)
    contact_number = models.CharField(max_length=13, null=True, blank=True, unique=True)
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
        return '{0}'.format(self.name)


class MedicineName(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    address = models.CharField(max_length=500, null=False)
    contact_number = models.CharField(max_length=13, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Stock(models.Model):
    def stock_number_incrementor():
        stock_table_count = Stock.objects.count()
        stock_number = "SCSNO#{0}".format(stock_table_count + 1)
        return stock_number

    stock_number = models.CharField(max_length=20, null=False, default=stock_number_incrementor, unique=True)
    medicine = models.ForeignKey(MedicineName, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(MedicalCompany, on_delete=models.DO_NOTHING)
    available_stock = models.PositiveIntegerField(null=False, blank=False, default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=5, null=False, blank=True)
    expiry_date = models.DateField(null=False)

    class Meta:
        unique_together = [
            ("medicine", "company"),
        ]

    def __str__(self):
        return '{0}'.format(self.medicine)


class Purchase(models.Model):
    purchase_number = models.CharField(max_length=250, editable=False, unique=True)
    medical_rep = models.ForeignKey(MedicalRep, null=False, on_delete=models.DO_NOTHING)
    medicine_name = models.ForeignKey(MedicineName, null=False, blank=False, on_delete=models.DO_NOTHING)
    company_name = models.ForeignKey(MedicalCompany, null=False, blank=False, on_delete=models.DO_NOTHING)
    brand_name = models.ForeignKey(Branding, null=True, blank=True, on_delete=models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=12, decimal_places=5, null=False, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    expiry_date = models.DateField(null=False, blank=False)
    invoice_amount = models.DecimalField(max_digits=12, decimal_places=5, null=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.medicine_name


class Sales(models.Model):
    def sales_id_incrementor():
        sales_table_count = Sales.objects.count()
        sales_id = "SCSID#{0}".format(sales_table_count + 1)
        return sales_id

    sales_number = models.CharField(max_length=30, editable=False,
                                    default=sales_id_incrementor, unique=True)
    item = models.ForeignKey(Stock, to_field="stock_number", null=False, blank=False, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    unit_price = models.DecimalField(max_digits=12, decimal_places=5, null=False, blank=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=5, null=False, blank=True)
    sale_date = models.DateField(auto_now_add=True, null=False)

    class Meta:
        verbose_name_plural = "Sales"


class Billing(models.Model):
    bill_number = models.CharField(max_length=200, editable=False, unique=True)
    BILL_TYPE_CHOICE_TUPLE = (('SB', "Sales Bill"), ('PB', "Purchase Bill"))
    bill_type = models.CharField(max_length=3, choices=BILL_TYPE_CHOICE_TUPLE, null=False)
    purchase_id = models.ForeignKey(Purchase, to_field="purchase_number", on_delete=models.DO_NOTHING)
    medical_rep = models.ForeignKey(MedicalRep, null=True, blank=True, on_delete=models.DO_NOTHING)
    sales = models.ForeignKey(Sales, to_field="sales_number", null=True, blank=True, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.DO_NOTHING)
    total_amount = models.DecimalField(max_digits=12, decimal_places=5, null=False)
    billing_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Billing"
        unique_together = [
            ("purchase_id", "medical_rep"),
            ("sales", "patient")
        ]
