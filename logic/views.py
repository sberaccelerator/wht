from django.shortcuts import render
from django.http import HttpResponse


def start_page(request):
    return render(request, "pages/start_page.html")


def article(request):
    return render(request, "pages/article.html")


def db(request):
    return HttpResponse("db")
