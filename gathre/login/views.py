from django.shortcuts import render
from django.http import HttpResponse

def loginPageView(request):
    return HttpResponse('Login Page')
