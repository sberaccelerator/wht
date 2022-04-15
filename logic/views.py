from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Greeting


def start_page(request):
    #return HttpResponse("test")
    return render(request, "pages/start_page.html")


def article(request):
    return render(request, "pages/article.html")


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "!notUsing/db.html", {"greetings": greetings})
