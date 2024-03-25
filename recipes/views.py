'''Views from my app recipes'''

# from django.http import HttpResponse  # type: ignore[import-untyped]
from django.shortcuts import render  # type: ignore[import-untyped]


def home(request):
    '''View home'''
    context = {
        'site_title': 'Recipes',
    }
    return render(
        request,
        'recipes/pages/home.html',
        context,
    )
