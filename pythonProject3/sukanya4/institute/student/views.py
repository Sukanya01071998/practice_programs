from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.status import HTTP_400_BAD_REQUEST


def talent(request):
    return HttpResponse("python")
from rest_framework.views import APIView
from .serializers import StudentSerializers
from .models import Student
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

class StudentCurd(APIView):
    # permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        if pk:
            student = get_object_or_404(Student, id=pk)
            student_serializers = StudentSerializers(student)
            return Response(student_serializers.data, status=status.HTTP_200_OK)
        else:
            students_qs = Student.objects.all()
            student_serializers = StudentSerializers(students_qs, many=True)
            return Response(student_serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        student_serializers = StudentSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        student = get_object_or_404(Student, id=pk)
        student_serializers = StudentSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def delete(self,request, pk=None, format=None):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.
