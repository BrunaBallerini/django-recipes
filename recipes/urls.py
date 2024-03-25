'''Url's from my app recipes'''

from django.urls import path  # type: ignore[import-untyped]

from recipes.views import my_view_about, my_view_home

urlpatterns = [
    path('', my_view_home),
    path('sobre/', my_view_about),
]
