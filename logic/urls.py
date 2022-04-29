from django.urls import path
from .views import *
from django.urls import include

app_name = 'logic'
urlpatterns = [
    path("", start_page, name="start_page"),
    path("article/", article, name="article"),
    path("db/", db, name="db"),
    path("accounts/", include("allauth.urls")),
]
