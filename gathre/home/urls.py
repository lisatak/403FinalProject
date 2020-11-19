from django.contrib import admin
from .views import indexPageView

urlpatterns = [
    path('', indexPageView, name='home'),
]