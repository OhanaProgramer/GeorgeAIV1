# georgeui/urls.py

from django.urls import path
from . import views

# recongize routes from http://localhost/ 

urlpatterns = [
    path("", views.home, name="home"),
]
