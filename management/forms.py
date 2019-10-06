from django import forms
from django.utils.safestring import mark_safe
from datetime import datetime
from .models import Course

class RegisterStudent(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    course = forms.ChoiceField(choices=[(course.course_id, course) for course in Course.objects.all()], widget=forms.Select(attrs={'class' : 'form-control'}))
    enrollment_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    #end_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

class EditStudentDetails(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    course = forms.ChoiceField(choices=[(course.course_id, course) for course in Course.objects.all()], widget=forms.Select(attrs={'class' : 'form-control'}))
    enrollment_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    #end_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

class AddCourse(forms.Form):
    course_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    course_level = forms.ChoiceField(choices=(('Bachelors', 'Bachelors'),('Masters', 'Masters'),), widget=forms.Select(attrs={'class' : 'form-control'}))
    course_duration_in_months = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    course_mode = forms.ChoiceField(choices=(('Part-Time', 'Part-Time'),('Full-Time', 'Full-Time'),), widget=forms.Select(attrs={'class' : 'form-control'}))
    course_credits = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    course_fees = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))

class EditCourseDetails(forms.Form):
    course_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    course_level = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    course_duration_in_months = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    course_mode = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    course_credits = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    course_fees = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
