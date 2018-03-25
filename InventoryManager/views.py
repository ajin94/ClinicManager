from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def pharmacy_index(request):

    # if request.session['login_status']:
    #     return render(request, 'InventoryManager/index.html', {"page_name": "index"})
    # else:
    #     return HttpResponse("no session")
    return render(request, 'InventoryManager/login.html', {"page_name": "index", "login_status": True})
