from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cidade/", views.receber_cidade, name="cidade")
]