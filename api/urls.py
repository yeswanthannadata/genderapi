from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^details','api.views.details', name="details"),
    url(r'^index','api.views.index', name="index"),
    url(r'^final','api.views.final', name="final"),
]

