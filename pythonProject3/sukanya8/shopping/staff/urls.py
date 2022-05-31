from django.urls import path,include
from.views import talent
urlpatterns=[
    path("call/",talent)
]