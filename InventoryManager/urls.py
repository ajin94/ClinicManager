from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.pharmacy_index, name="pharmacy_index"),
    path('billing/', views.pharmacy_billing, name="pharmacy_billing"),
    path('purchase/', views.pharmacy_purchase, name="pharmacy_purchase"),
    path('billing/ajax/get_medicine_info/', views.get_medicine_info, name="get_medicine_info"),
]
