from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseBadRequest
from employee.forms import EmployeeForm
from employee.models import Employee

# Create your views here.
def List(request):
    empList = Employee.objects.all()
    print("Error : ", empList)
    return render(request,"list.html",{'emplist':empList})

def New(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/employee/list')
            except:
                pass
    else:
        empForm = EmployeeForm()
        return render(request,'new.html',{'form':empForm})

def edit(request,id):
    objEmp = Employee.objects.get(id=id)

    if request.method == "POST":
        
        form = EmployeeForm(request.POST,instance=objEmp)
        print("jjjkkkjkllllll")
        if form.is_valid():
            print("*********l")
            try:
                form.save()
                return redirect('/employee/list')
            except:
                pass
    else:
        return render(request,'edit.html',{'employee':objEmp})

def delete(request,id):
    objEmp = Employee.objects.get(id=id)
    objEmp.delete()
    return redirect('/employee/list')
