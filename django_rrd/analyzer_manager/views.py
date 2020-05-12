from django.http import HttpResponse
from django.shortcuts import render

from analyzer_manager.components.MainMenu.MainMenu import get_main_menu


# def index(request):
#     return render(request, "index.html")


def index(request):
    return get_main_menu(render, request)


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
