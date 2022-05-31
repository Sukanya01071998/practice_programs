
from django.urls import path,include
from.views import tweak
urlpatterns = [

    path('pop/',tweak),

]
