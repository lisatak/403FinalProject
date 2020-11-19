from django.contrib import admin
from .views import addPageView

urlpatterns = [
    path('', addPageView, name='home'),
]