from django.urls import path,include
from .views import *

urlpatterns = [
    path('index/',index),
    path("oneaddmore/",oneaddmore),
    path("onegetmore/",onegetmore),
    path("oneupdatemore/",oneupdatemore),
    path("onedelete/",onedelete),
]