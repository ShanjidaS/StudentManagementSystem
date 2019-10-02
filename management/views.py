from django.shortcuts import render, get_object_or_404
from .forms import RegisterStudent, EditStudentDetails
from django.contrib import messages
from . import models
from .models import Student
from django.shortcuts import redirect

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

def edit_student_details(request, studentid):
    student = Student.objects.get(pk=studentid)
    if request.method == 'POST':
        form = EditStudentDetails(request.POST)
        if form.is_valid():
            obj = models.Student()
            obj.student_id = student
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
    student = Student.objects.get(pk=studentid)
    context = {
        'student': student
    }
    return render(request, 'management/students/student-details.html', context)

def delete_student(request, studentid):
    student = Student.objects.get(pk=studentid)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student successfully deleted!")
        return redirect('management-students-view-all')

    context = {
        'student': student
    }
    return render(request, 'management/students/delete-student.html', context)
