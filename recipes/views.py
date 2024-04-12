'''Views from my app recipes'''

# from django.http import HttpResponse  # type: ignore[import-untyped]
from django.shortcuts import render  # type: ignore[import-untyped]

from utils.recipes.factory import make_recipe


def home(request):
    '''View home'''
    context = {
        'site_title': 'Home',
        'recipes': [make_recipe() for _ in range(9)],
        'is_detail_page': False,
    }
    return render(
        request,
        'recipes/pages/home.html',
        context,
    )


def recipe(request, id):
    '''View home'''
    context = {
        'site_title': 'Recipes',
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
    return render(
        request,
        'recipes/pages/recipe-view.html',
        context,
    )
