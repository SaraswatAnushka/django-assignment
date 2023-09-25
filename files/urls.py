from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path,include
from . import views


urlpatterns=[
    path('index',views.index,name='index'),
    path('view',views.show_files,name='showfile')
]