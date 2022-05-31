from django.shortcuts import render
from django.http import HttpResponse

def tweak(request):
    return HttpResponse("hello")
