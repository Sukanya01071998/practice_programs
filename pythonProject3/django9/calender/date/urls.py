from django.urls import path,include
from.views import inner
from.views import inner,index,create,edit,delete,update

urlpatterns=[
    path('call/',inner),
    path('index/',index),
    path('create/',create),
    path('edit/<str:name>/',edit),
    path('delete/<str:name>/',delete),
    path('update/<str:name>/',update)



]