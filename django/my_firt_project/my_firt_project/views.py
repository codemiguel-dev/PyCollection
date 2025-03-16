from django.http import HttpResponse


def saludo(request):
    return HttpResponse("hello")


def despedida(request):
    return HttpResponse("good bye")


def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("No eres mayor de edad")
