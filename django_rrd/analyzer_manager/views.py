from django.http import HttpResponse
from django.shortcuts import render

from analyzer_manager.components.MainMenu.MainMenu import main_menu_component


def index(request):
    return render(request, "index.html")


def main_menu(request):
    return main_menu_component(render, request)


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
