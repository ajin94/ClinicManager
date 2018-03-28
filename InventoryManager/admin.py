from django.contrib import admin
from .models import *


class AdminMedicalCompany(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']


class AdminBranding(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']


class AdminPurchase(admin.ModelAdmin):
    list_display = ['medicine_name', 'expiry_date', 'company_name', 'brand_name', 'quantity',
                    'unit_price', 'invoice_amount', 'created_date', 'updated_date']


class AdminMedicineName(admin.ModelAdmin):
    list_display = ['name']


class AdminMedicalRep(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'created_date', 'updated_date']


class AdminSales(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'sale_date']


class AdminBilling(admin.ModelAdmin):
    list_display = ['patient', 'bill_number', 'total_amount', 'billing_date']
    search_fields = ['bill_number']

admin.site.register(Purchase, AdminPurchase)
admin.site.register(Sales, AdminSales)
admin.site.register(Branding, AdminBranding)
admin.site.register(MedicalCompany, AdminMedicalCompany)
admin.site.register(MedicalRep, AdminMedicalRep)
admin.site.register(Billing, AdminBilling)
admin.site.register(MedicineName, AdminMedicineName)

admin.site.site_title = "Inventory Management"
