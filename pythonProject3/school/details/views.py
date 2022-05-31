from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def summery(request):
    return HttpResponse("sukanya")
def Http(request):
    return HttpResponse("prabha")
def Response(request):
    return HttpResponse("naga")
