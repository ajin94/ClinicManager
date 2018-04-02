from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import PurchaseBillingForm
from datetime import datetime
from .models import Billing, Purchase, MedicalRep, MedicalCompany


def pharmacy_index(request):
    return render(request, 'InventoryManager/index.html', {"page_name": "index", "login_status": True})


def pharmacy_billing(request):
    return render(request, 'InventoryManager/billing.html', {"page_name": "billing", 'dated': datetime.now(),
                                                             "login_status": True})


def get_medicine_info(request):
    print(request)
    if request.method == 'GET':
        # item_id = int(request.GET.get('medicine_item_id'))
        item_id = 1
        # item_dict = {}
        return HttpResponse(item_id)


def pharmacy_purchase(request):
    purchase_data_count = Purchase.objects.count()
    purchase_number = "SCPID#{0}".format(purchase_data_count + 1)
    medical_rep_id = MedicalRep.objects.count()+1
    medical_company_id = MedicalCompany.objects.count() + 1
    return render(request, 'InventoryManager/purchase.html', {"page_name": "purchase", 'dated': datetime.now(),
                                                              "login_status": True, "form": PurchaseBillingForm,
                                                              "purchase_number": purchase_number,
                                                              "medical_rep_id": medical_rep_id,
                                                              "medical_company_id":medical_company_id})
