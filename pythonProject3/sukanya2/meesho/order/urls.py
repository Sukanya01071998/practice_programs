from django.urls import path,include
from.views import tech,index,create,edit,delete,update,login,user_logout,home
urlpatterns=[
    path("call/",tech),
    path("index/",index),
    path('create/',create),
    path('edit/<str:name>/',edit),
    path('delete/<str:name>/',delete),
    path('update/<str:name>/',update),
    path('login/',login),
    path('logout/',user_logout),
    path('home/',home),

]