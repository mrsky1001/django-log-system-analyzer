from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return render(request, "index.html")
from analyzer_manager.definitions import render_list_rrd


def index(request):
    return list_rrd(request)


def list_rrd(request):
    return render_list_rrd(render, request)


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
