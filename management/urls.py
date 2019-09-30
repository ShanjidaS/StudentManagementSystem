from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='management-home'),
    path('students/', views.students, name='management-students'),
]