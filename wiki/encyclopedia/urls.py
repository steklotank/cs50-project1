from django.urls import path

from . import views
    
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("create/", views.create, name="create"),
    path("randomize/", views.randomize, name="randomize")
]
