from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
