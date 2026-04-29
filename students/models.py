from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    registration_number = models.CharField(max_length=20, unique=True)
    telephone_number = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_full_name()


class Note(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Course(models.Model):
    course_name = models.CharField(max_length=255, null=False)
    course_code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.course_code

ACTIVE = "active"
DROPPED = "dropped"
COMPLETED = "completed"

active_state = [
        (ACTIVE, "active"),
        (DROPPED, "dropped"),
        (COMPLETED, "completed"),
    ]  

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  
    status = models.CharField(max_length=10, choices=active_state, default=ACTIVE)
    enrolled_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.course.course_code}"
    
class Attendance(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.course.course_code}"

class Grade(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.course.course_code}"
    

