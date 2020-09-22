from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# the view is a controller

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def helloWorld(request):
    return HttpResponse("python study");