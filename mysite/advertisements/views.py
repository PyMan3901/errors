from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return render(requests, 'index.html')






# Create your views here.
