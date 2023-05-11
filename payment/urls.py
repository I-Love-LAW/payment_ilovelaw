from django.urls import path
from . import views

urlpatterns = [
    path("create-payment", views.PembayaranView.as_view())
]