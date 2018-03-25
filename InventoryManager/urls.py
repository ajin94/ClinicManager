from django.urls import path
from . import views

urlpatterns = [
    path('', views.pharmacy_index, name="pharmacy_index"),
]
