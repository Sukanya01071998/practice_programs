from django.contrib import admin
from django.urls import include, path
from .views import summery,Http,Response
urlpatterns = [
    path('sukanya/',summery),
    path('prabha/',Http),
    path('naga/',Response)




]

