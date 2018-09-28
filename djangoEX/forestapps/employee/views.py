from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods

# Create your views here.
def hello(request):  
    return HttpResponse("<h1> employee / views go!</h1>")  