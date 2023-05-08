from django.urls import path
from . import views

urlpatterns = [
    path("upgrade-membership", views.PembayaranView.as_view())
]