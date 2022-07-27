from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('tweets/<int:id>/', views.tweets, name='tweets'),
  path('template/', views.template, name='template'),
  path('dynamic/<str:name>/', views.dynamic, name='dynamic')
]
