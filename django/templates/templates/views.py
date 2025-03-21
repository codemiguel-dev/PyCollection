from django.shortcuts import render


def simple(request):
    return render(request, "home.html", {})


def dinamico(request, name):
    categories = ["code", "design", "marketing", "finanzas"]
    context = {"name": name, "categories": categories}
    return render(request, "dinamico.html", context)
