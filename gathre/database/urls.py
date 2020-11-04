from django.urls import path
from .views import databasePageView

urlpatterns = [
    path("", databasePageView, name="database")
]
