'''Views from my app recipes'''

# from django.http import HttpResponse  # type: ignore[import-untyped]
from django.shortcuts import render  # type: ignore[import-untyped]


def my_view_home(request):
    '''View home'''
    context = {
        'site_title': 'Recipes',
    }
    return render(
        request,
        'recipes/home.html',
        context,
    )


def my_view_about(request):
    '''View about'''
    context = {
        'site_title': 'About',
    }
    return render(
        request,
        'recipes/home.html',
        context,
    )
