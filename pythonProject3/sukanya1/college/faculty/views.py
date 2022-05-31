from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Employee
from.forms import EmployeeForm
from django.contrib.auth import authenticate,logout
def inner(request):
    return HttpResponse("python")
def tweak(request):
    return HttpResponse("django")

def index(request):
    DRDO_data=Employee.objects.all()
    return render(request,"index.html",{'DRDO_data':DRDO_data})

def create(request):
    if request.method=='POST':
        print(request.POST)
        form=EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect("/index/")
    else:
        form=EmployeeForm()
    return render(request,'create.html',{'form':form})

def edit(request,name):
    DRDO_data=Employee.objects.get(name=name)
    form=EmployeeForm(instance=DRDO_data)
    return render(request,'update.html',{'form':form,'name':name})

def delete(request,name):
    DRDO_data=Employee.objects.get(name=name)
    print("DRDO_data", DRDO_data)
    DRDO_data.delete()
    return redirect("/index/")

def update(request,name):
    DRDO_data=Employee.objects.get(name=name)
    form=EmployeeForm(request.POST,instance=DRDO_data)
    if form.is_valid():
        form.save()
        return redirect("/index/")
    return render(request,'update.html',{'form':form,'name':name})
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


# Create your views here.
