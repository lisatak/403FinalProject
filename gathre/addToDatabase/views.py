from django.shortcuts import render
from django.http import HttpResponse


def addPageView(request):
    return render(request, 'add/index.html')
