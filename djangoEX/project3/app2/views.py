from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods



def displaytemplate2(request):
	template = loader.get_template('index2.html')
	return HttpResponse(template.render())


def employee1 (request):
	template = loader.get_template('employee/index.html')
	return HttpResponse(template.render())


#@require_http_methods(["POST"])
def show(request):
    return HttpResponse("<h1>TEST POST Func </h1>")  

def hello(request):  
    return HttpResponse("<h1>app1 / views go!</h1>")  