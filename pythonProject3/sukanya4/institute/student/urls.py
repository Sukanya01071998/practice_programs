from django.urls import path,include
from .views import talent, Student, StudentCurd,login

urlpatterns=[
    path("nandhu/",talent),
    path('students', StudentCurd.as_view()),
    path('students/<int:pk>/', StudentCurd.as_view()),
    path('api/login', login),
]