from django.shortcuts import render
from django.http import HttpResponse


def databasePageView(request):
    return HttpResponse('Database page')
