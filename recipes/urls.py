'''Url's from my app recipes'''

from django.urls import path  # type: ignore[import-untyped]

from recipes.views import home  # type: ignore[no-name-in-module]

urlpatterns = [
    path('', home),
]
