from django.urls import path
from .views import addPageView

urlpatterns = [
    path('', addPageView, name='add'),
]