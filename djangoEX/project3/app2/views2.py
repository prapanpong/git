from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  
  
def hello(request):  
    return HttpResponse("<h1>Hello, Welcome to Django!VIEW 2</h1>")  