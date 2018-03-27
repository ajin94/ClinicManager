from django.urls import path
from . import views

urlpatterns = [
    path('', views.pharmacy_index, name="pharmacy_index"),
    path('billing/', views.pharmacy_billing, name="pharmacy_billing"),

    # ajax requests
    path('ajax/get_medicine_info/', views.get_medicine_info, name="get_medicine_info"),
]
