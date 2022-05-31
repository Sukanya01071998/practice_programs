from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
from.forms import studentForm
from django.contrib.auth import authenticate,logout


def inner(request):
    return HttpResponse("sindhu")
def index(request):
    DRDO_data=student.objects.all()
    return render(request,"index.html",{'DRDO_data':DRDO_data})

def create(request):
    if request.method=='POST':
        print(request.POST)
        form=studentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect("/index/")
    else:
        form=studentForm()
    return render(request,'create.html',{'form':form})

def edit(request,name):
    DRDO_data=student.objects.get(name=name)
    form=studentForm(instance=DRDO_data)
    return render(request,'update.html',{'form':form,'name':name})

def delete(request,name):
    DRDO_data=student.objects.get(name=name)
    print("DRDO_data", DRDO_data)
    DRDO_data.delete()
    return redirect("/index/")

def update(request,name):
    DRDO_data=student.objects.get(name=name)
    form=studentForm(request.POST,instance=DRDO_data)
    if form.is_valid():
        form.save()
        return redirect("/index/")
    return render(request,'update.html',{'form':form,'name':name})

