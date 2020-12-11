"""IMDB URL Configuration
"""
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('push/', views.pushdata_db, name='push'),
    url(r'search/', views.search, name='search'),
]

