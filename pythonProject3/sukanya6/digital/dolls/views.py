from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import StudentSerializers
from .models import Student
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.AllowAny]
def func(request):
    return HttpResponse("veeksha")

# Create your views here.
