from django.urls import path
from . import views

app_name = "conta_energia"

urlpatterns = [
    path('', views.index, name = 'conta_energia'),
]
