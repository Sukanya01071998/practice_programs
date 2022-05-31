from django.urls import path,include
from .views import  students_list_or_create, students_get_or_update

urlpatterns=[
    # path("call/",inner),
    path('students/', students_list_or_create),
    path('students/<int:pk>/', students_get_or_update),
]