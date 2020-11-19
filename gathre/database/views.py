from django.shortcuts import render
from django.http import HttpResponse


def databasePageView(request):
    return render(request, 'database/index.html')
