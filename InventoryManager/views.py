# from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import BillingForm
from datetime import datetime
# Create your views here.


def pharmacy_index(request):
    return render(request, 'InventoryManager/index.html', {"page_name": "index", "login_status": True})


def pharmacy_billing(request):
    billing_form = BillingForm()
    # bill-count =
    return render(request, 'InventoryManager/billing.html', {"page_name": "billing", "login_status": True,
                                                             'form': billing_form, 'dated': datetime.now(),
                                                             'bill_number': 1})


def get_medicine_info(request):
    pass
