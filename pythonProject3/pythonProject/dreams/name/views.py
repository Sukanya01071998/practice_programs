from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employee
from .forms import *


def talent(request):
    return HttpResponse('<h1>subrahmanyam</h1>')


def index(request):
    DRDO_data=Employee.objects.all()[2:]
    return render(request,"index.html",{'DRDO_data':DRDO_data})

def create(request):
    if request.method=='POST':
        print(request.POST)
        form=EmployeeForms(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/index/")
    else:
            form=EmployeeForms()
    return render(request,'create.html',{'form':form})
def edit(request,eid):
    DRDO_data=Employee.objects.get(eid=eid)
    form=EmployeeForms(instance=DRDO_data)
    return render(request,"update.html",{'form':form,'eid':eid})

def update(request,eid):
    DRDO_data=Employee.objects.get(eid=eid)
    form=EmployeeForms(request.POST,instance=DRDO_data)
    if form.is_valid():
        form.save()
        return redirect("/index/")
    return render(request,"update.html",{'form':form,'eid':eid})

def delete(request,eid):
    DRDO_data=Employee.objects.get(eid=eid)
    print("DRDO_data",DRDO_data)
    DRDO_data.delete()
    return redirect("/index/")


def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('password')
        user=authenticate(username=uname,password=pwd)
        print(user)
        if user:
            return redirect('/index/')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login/')

def home(request):
    return render(request,'home.html')




