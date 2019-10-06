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
    path('students/delete-student/<int:studentid>', views.delete_student, name='management-students-delete-student'),

    path('courses/', views.courses, name='management-courses'),
    path('courses/add-course', views.add_course, name='management-courses-add-course'),
    path('courses/view-all', views.view_all_courses, name='management-courses-view-all'),
    path('courses/course-details/<int:course_id>', views.course_details, name='management-courses-course-details'),
    path('courses/edit-details/<int:course_id>', views.edit_course_details, name='management-courses-edit-details'),
    path('courses/delete-course/<int:course_id>', views.delete_course, name='management-courses-delete-course'),
    
    path('summary/', views.summary, name='management-summary'),
]