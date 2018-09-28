from django.shortcuts import render
from django.template import loader
from app1.form import loginForm
from django.http import HttpResponse
from app1.form import EmployeeForm

# Create your views here.



def displaytemplate1 (request):
    template = loader.get_template('index1.html')
    return HttpResponse(template.render())

def employee (request):
    template = loader.get_template('/employee/index.html')
    return HttpResponse(template.render())

def hello(request):
    return HttpResponse("<h1>Hello, Welcome to Django!</h1>")

def html1 (request):
    template = loader.get_template('showstatic.html')
    return HttpResponse(template.render())

def displayname(request):

    template = loader.get_template('index1.html')
    name = {
        'fullname' : 'adadasds',
        'age' : '43',
        'school' : 'vbbbbbbbb'
        }
    return HttpResponse(template.render(name))

def displayLoginForm (request):
    login = loginForm()
    return render(request,"logInForm.html",{'form':login})

def displayEmployeeForm (request):
    emp = EmployeeForm()
    return render(request,"employee.html",{'form':emp})

def createSession(request):
    request.session['uid'] = 1
    request.session['name'] = "John Doe"
    return HttpResponse("Ceart session complete")

def displaySession(request):
    myData = "ID: " + str(request.session['uid'])+ "<br>Name: " + str(request.session['name'])
    return HttpResponse(myData)