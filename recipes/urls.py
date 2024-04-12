# pylint: disable-msg=C0103
'''Url's from my app recipes'''

from django.urls import path  # type: ignore[import-untyped]

from recipes import views  # type: ignore[no-name-in-module]

app_name = 'recipe'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
