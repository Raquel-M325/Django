from django.urls import path
from . import views

app_name = "emprestimo"

urlpatterns = [
    path("", views.index, name = "emprestimo"),
]