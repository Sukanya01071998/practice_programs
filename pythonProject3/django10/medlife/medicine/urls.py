from django.contrib.admindocs import views
from django.contrib.sitemaps.views import index
from django.urls import path
from.views import talent,index,creata,edit,update,delete,login,logout,home

urlpatterns=[
    path('how/', talent),
    path('index/', index),
    path('creata/', creata),
    path("edit/<str:eid>/", edit),
    path("update/<str:eid>/", update),
    path("delete/<str:eid>/",delete),
    path('login/', login),
    path('user_logout/', logout),
    path('home/', home)
]