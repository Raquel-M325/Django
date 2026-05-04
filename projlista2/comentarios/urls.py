from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("comentario/", views.envie_comentario, name="envie_comentario"),
]