from django.shortcuts import render, get_object_or_404
from .forms import RegisterStudent, EditStudentDetails, AddCourse, EditCourseDetails
from django.contrib import messages
from . import models
from .models import Student, Course
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

# Home functions

def home(request):
    return render(request, 'management/home.html')

def students(request):
    return render(request, 'management/students/students.html')

def register_student(request):
    if request.method == 'POST':
        form = RegisterStudent(request.POST)
        if form.is_valid():
            obj = models.Student()
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            obj.date_of_birth = form.cleaned_data['date_of_birth']
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
            obj.address = form.cleaned_data['address']
            obj.degree_name = form.cleaned_data['degree_name']
            obj.start_date = form.cleaned_data['start_date']
            obj.end_date = form.cleaned_data['end_date']
            obj.save()
            messages.success(request, f'Student successfully registered!' )
    else:
        form = RegisterStudent()
    return render(request, 'management/students/register.html', {'form' : form})

def edit_student_details(request, studentid):
    try:
        student = Student.objects.get(pk=studentid)
    except ObjectDoesNotExist:
        return redirect('management-students-view-all')
        
    if request.method == 'POST':
        form = EditStudentDetails(request.POST)
        if form.is_valid():
            obj = models.Student()
            obj.student_id = student.student_id
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            obj.date_of_birth = form.cleaned_data['date_of_birth']
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
            obj.address = form.cleaned_data['address']
            obj.degree_name = form.cleaned_data['degree_name']
            obj.start_date = form.cleaned_data['start_date']
            obj.end_date = form.cleaned_data['end_date']
            obj.save()
            messages.success(request, f'Student has been edited' )
    else:
        form = EditStudentDetails(initial={
            'first_name': student.first_name,
            'last_name': student.last_name,
            'date_of_birth': student.date_of_birth,
            'email': student.email,
            'phone': student.phone,
            'address': student.address,
            'degree_name': student.degree_name,
            'start_date': student.start_date,
            'end_date': student.end_date,
        })
    return render(request, 'management/students/edit-details.html', {'form' : form})

def view_all_students(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'management/students/view-all.html', context)

def student_details(request, studentid):
    try:
        student = Student.objects.get(pk=studentid)
    except ObjectDoesNotExist:
        return redirect('management-students-view-all')

    context = {
        'student': student
    }
    return render(request, 'management/students/student-details.html', context)

def delete_student(request, studentid):
    try:
        student = Student.objects.get(pk=studentid)
    except ObjectDoesNotExist:
        return redirect('management-students-view-all')

    if request.method == 'POST':
        student.delete()
        messages.success(request, f'Student has been deleted' )
        return redirect('management-students-view-all')

    context = {
        'student': student
    }
    return render(request, 'management/students/delete-student.html', context)

# Course functions

def courses(request):
    return render(request, 'management/courses/courses.html')

def add_course(request):
    if request.method == 'POST':
        form = AddCourse(request.POST)
        if form.is_valid():
            obj = models.Course()
            obj.course_name = form.cleaned_data['course_name']
            obj.course_level = form.cleaned_data['course_level']
            obj.course_duration_in_months = form.cleaned_data['course_duration_in_months']
            obj.course_mode = form.cleaned_data['course_mode']
            obj.course_credits = form.cleaned_data['course_credits']
            obj.save()
            messages.success(request, f'Course successfully added!' )
    else:
        form = AddCourse()
    return render(request, 'management/courses/add-course.html', {'form' : form})

def view_all_courses(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, 'management/courses/view-all.html', context)

def course_details(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return redirect('management-courses-view-all')
    context = {
        'course': course
    }
    return render(request, 'management/courses/course-details.html', context)

def edit_course_details(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return redirect('management-courses-view-all')
        
    if request.method == 'POST':
        form = EditCourseDetails(request.POST)
        if form.is_valid():
            obj = models.Course()
            obj.course_id = course.course_id
            obj.course_name = form.cleaned_data['course_name']
            obj.course_level = form.cleaned_data['course_level']
            obj.course_duration_in_months = form.cleaned_data['course_duration_in_months']
            obj.course_mode = form.cleaned_data['course_mode']
            obj.course_credits = form.cleaned_data['course_credits']
            obj.course_fees = form.cleaned_data['course_fees']
            obj.save()
            messages.success(request, f'Course has been edited' )
    else:
        form = EditCourseDetails(initial={
            'course_name': course.course_name,
            'course_level': course.course_level,
            'course_duration_in_months': course.course_duration_in_months,
            'course_mode': course.course_mode,
            'course_credits': course.course_credits,
            'course_fees': course.course_fees,
        })
    return render(request, 'management/courses/edit-details.html', {'form' : form})

def delete_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except ObjectDoesNotExist:
        return redirect('management-courses-view-all')

    if request.method == 'POST':
        course.delete()
        messages.success(request, f'Course has been deleted' )
        return redirect('management-courses-view-all')

    context = {
        'course': course
    }
    return render(request, 'management/courses/delete-course.html', context)