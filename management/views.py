from django.shortcuts import render

def home(request):
    return render(request, 'management/home.html')

def students(request):
    return render(request, 'management/students.html')

