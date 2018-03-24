from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_sales, name="make_sales"),
]
