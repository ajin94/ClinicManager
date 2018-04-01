from django.contrib import admin
from .models import *


class AdminMedicalCompany(admin.ModelAdmin):
    list_display = ['name', 'address', 'contact_number', 'created_date', 'updated_date']


class AdminBranding(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date']


class AdminPurchase(admin.ModelAdmin):
    list_display = ['purchase_number', 'medicine_name', 'medical_rep', 'company_name', 'brand_name', 'expiry_date',
                    'quantity', 'unit_price', 'invoice_amount', 'created_date', 'updated_date']
    search_fields = ['purchase_number']


class AdminMedicineName(admin.ModelAdmin):
    list_display = ['name']


class AdminMedicalRep(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'contact_number', 'created_date', 'updated_date']


class AdminSales(admin.ModelAdmin):
    list_display = ['sales_number', 'item', 'quantity', 'unit_price', 'total_price', 'sale_date']
    search_fields = ['sales_number']


class AdminBilling(admin.ModelAdmin):
    list_display = ['bill_number', 'purchase_id', 'medical_rep', 'sales', 'patient', 'total_amount', 'billing_date']
    search_fields = ['bill_number']

admin.site.register(Purchase, AdminPurchase)
admin.site.register(Sales, AdminSales)
admin.site.register(Branding, AdminBranding)
admin.site.register(MedicalCompany, AdminMedicalCompany)
admin.site.register(MedicalRep, AdminMedicalRep)
admin.site.register(Billing, AdminBilling)
admin.site.register(MedicineName, AdminMedicineName)

admin.site.site_title = "Inventory Management"
