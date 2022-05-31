from django.urls import path,include
from .views import home, StudentCurd, StudentCurdd
from rest_framework_simplejwt import views as jwt_views

urlpatterns=[
    path("call/",home),
    path('students', StudentCurd.as_view(), name="students_list_or_create"),
    path('students/<int:pk>/', StudentCurdd.as_view(), name="students_get_or_update"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]