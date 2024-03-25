'''Views from my app recipes'''

from django.http import HttpResponse  # type: ignore[import-untyped]

# from django.shortcuts import render


def my_view_home(request):
    '''View home'''
    return HttpResponse('home')


def my_view_about(request):
    '''View about'''
    return HttpResponse('about')
