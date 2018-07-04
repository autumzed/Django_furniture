from django.shortcuts import render
from django.db import connection


def index(request):
    return render(request, 'index.html')
