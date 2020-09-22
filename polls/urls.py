from django.urls import path
from . import views

urlpatterns=[
    path('hello/wrold', views.helloWorld, name="hello"),
    path('index' ,views.index, name="index")
]