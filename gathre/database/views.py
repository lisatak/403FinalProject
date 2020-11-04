from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def databasePageView(request):
    return HttpResponse('Database page')
