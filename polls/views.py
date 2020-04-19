from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse

def helloWorld(request):
    return HttpResponse("python study");