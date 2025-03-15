from django.shortcuts import render

from .models import Noticia


def home(request):
    noticias = Noticia.objects.all()
    return render(request, "sitio_principal/home.html", {"noticias": noticias})
