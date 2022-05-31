from django.shortcuts import render
from django.http import HttpResponse
import datetime

def datetime_view(request):
    date = datetime.datetime.now()
    s='<h1> The current date & time @ server is:' + str(date) + '</h1>'
    return HttpResponse(s)



