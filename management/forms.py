from django import forms
from django.utils.safestring import mark_safe
from datetime import datetime

class RegisterStudent(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    degree_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

class EditStudentDetails(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    degree_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
