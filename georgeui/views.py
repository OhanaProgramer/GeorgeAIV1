# georgeui/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to GeorgeAIV1 Dashboard</h1>")