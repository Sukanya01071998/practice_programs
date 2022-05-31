from django.urls import path,include
from.views import StudentCurd
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'students',StudentCurd,basename="students")

urlpatterns=[
    path("",include(router.urls))

]