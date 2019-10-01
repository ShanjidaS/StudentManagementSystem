from django.shortcuts import render, get_object_or_404
from .forms import RegisterStudent
from django.contrib import messages
from . import models
from .models import Student

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
            messages.success(request, f'Student registered!' )
    else:
        form = RegisterStudent()
    return render(request, 'management/students/register.html', {'form' : form})

def view_all_students(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'management/students/view-all.html', context)

def student_details(request, studentid):
    student = Student.objects.get(pk=studentid)
    context = {'student': student}
    return render(request, 'management/students/student-details.html', context)