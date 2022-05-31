from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# def inner(request):
#     return HttpResponse("django")
from .serializers import EmployeeSerializers
from .models import Employee
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def students_list_or_create(request):
    if request.method == "GET":
        students_qs =  Employee.objects.all()
        student_serializers =  EmployeeSerializers(students_qs, many=True)
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    else:
        student_serializers =  EmployeeSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def students_get_or_update(request, pk):
    student = get_object_or_404( Employee, id=pk)
    if request.method == "GET":
        student_serializers = EmployeeSerializers(student)
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        student_serializers =  EmployeeSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.
