from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("frete/", views.frete, name="frete"),
]