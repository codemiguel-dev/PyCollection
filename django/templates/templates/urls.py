from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("simples/", views.simple, name="simple"),
    # uso de srting para pasar contexto.
    path("dinamico/<str:name>", views.dinamico, name="dinamico"),
]
