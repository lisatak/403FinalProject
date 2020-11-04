from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def loginPageView(request):
    return HttpResponse('Login Page')
