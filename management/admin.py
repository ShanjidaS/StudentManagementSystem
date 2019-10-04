from django.contrib import admin
from .models import Person, Student, Course

admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Course)