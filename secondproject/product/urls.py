from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('',home1),
    path('add/',productMainmodel_post),
    path('view/<int:id>/',imgview),
]