from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='management-home'),
    path('students/', views.students, name='management-students'),
    path('students/register/', views.register_student, name='management-students-register'),
    path('students/view-all/', views.view_all_students, name='management-students-view-all'),
    path('students/student-details/<int:studentid>', views.student_details, name='management-students-student-details'),
    path('students/edit-details/<int:studentid>', views.edit_student_details, name='management-students-edit-details'),
]