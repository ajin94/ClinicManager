from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import BillingForm, PurchaseForm
from datetime import datetime
from .models import Billing, Purchase
# Create your views here.


def pharmacy_index(request):
    return render(request, 'InventoryManager/index.html', {"page_name": "index", "login_status": True})


def pharmacy_billing(request):
    billing_form = BillingForm()
    bill_count = Billing.objects.count()
    bill_number = "SCBN#{0}".format(bill_count+1)
    return render(request, 'InventoryManager/billing.html', {"page_name": "billing", "login_status": True,
                                                             'form': billing_form, 'dated': datetime.now(),
                                                             'bill_number': bill_number})


def get_medicine_info(request):
    print(request)
    if request.method == 'GET':
        # item_id = int(request.GET.get('medicine_item_id'))
        item_id = 1
        # item_dict = {}
        return HttpResponse(item_id)


def pharmacy_purchase(request):
    purchase_form = PurchaseForm()
    purchase_count = Purchase.objects.count()
    purchase_id = "SCPID#{}".format(purchase_count)
    return render(request, 'InventoryManager/purchase.html', {"page_name": "purchase", "login_status": True,
                                                              'form': purchase_form, 'dated': datetime.now(),
                                                              'purchase_id': purchase_id})
