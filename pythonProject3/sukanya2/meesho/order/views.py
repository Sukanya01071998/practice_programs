from django.shortcuts import render,redirect
from.models import Customer
from .forms import  CustomerForm
from django.contrib.auth import authenticate,logout
from django.http import HttpResponse
def tech(request):
    return HttpResponse("how are you")
def index(request):
    DRDO_data=Customer.objects.all()
    return render(request,"index.html",{'DRDO_data':DRDO_data})

def create(request):
    if request.method=='POST':
        print(request.POST)
        form=CustomerForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect("/index/")
    else:
        form=CustomerForm()
    return render(request,'create.html',{'form':form})

def edit(request,name):
    DRDO_data=Customer.objects.get(name=name)
    form=CustomerForm(instance=DRDO_data)
    return render(request,'update.html',{'form':form,'name':name})

def delete(request,name):
    DRDO_data=Customer.objects.get(name=name)
    print("DRDO_data", DRDO_data)
    DRDO_data.delete()
    return redirect("/index/")

def update(request,name):
    DRDO_data=Customer.objects.get(name=name)
    form=CustomerForm(request.POST,instance=DRDO_data)
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
