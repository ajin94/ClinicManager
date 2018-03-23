from django.urls import path
from . import views

urlpatterns = [
    path('sales/add/', views.make_sales, name="make_sales"),
]
