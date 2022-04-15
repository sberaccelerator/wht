from django.urls import path
from .views import *

from .views import *

app_name = 'logic'
urlpatterns = [
    path("", start_page, name="start_page"),
    path("article/", article, name="article"),
    path("db/", db, name="db"),
]
