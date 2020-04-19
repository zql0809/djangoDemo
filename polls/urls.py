from django.urls import  path
from . import views

urlpatterns=[
    path('adsa/aa',views.helloWorld,name="hello")
]