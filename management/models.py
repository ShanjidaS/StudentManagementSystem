from django.db import models

class Person(models.Model):
    person_id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Student(Person):
    student_id = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    degree_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Course(models.Model):
    course_id = models.AutoField(primary_key=True) 
    course_name = models.CharField(max_length=100)
    course_level = models.CharField(max_length=50)
    course_duration_in_months = models.IntegerField()
    course_mode = models.CharField(max_length=50)
    course_credits = models.IntegerField()
    course_fees = models.IntegerField(null=False)
    objects = models.Manager()

    def __str__(self):
        return self.course_name