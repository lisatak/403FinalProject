from django.shortcuts import render
from django.http import HttpResponse


def addPageView(request):
    return HttpResponse('Database page')
