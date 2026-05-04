from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("comentarios/", include("comentarios.urls")),
    path("previsao/", include("previsao.urls")),
    path("fretes/", include("fretes.urls")),
]