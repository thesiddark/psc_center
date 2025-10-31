from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from utility.models import BaseModel
User = get_user_model()
# Create your models here.
class Student(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=(("m","Male"),("f","Female"),("o","Other")))
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    emergency_contact = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    status = models.CharField(max_length=1,choices=(("a","Active"),("s","Suspended"),("w","Withdrawn")))
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateField()
    
    

def __str__(self):
    return f"{self.id} : {self.first_name} {self.last_name}"

class Enrollment(BaseModel):
    STATUS_CHOICES = (
        ('a', 'Archived'),
        ('p', 'Published'),
        ('d', 'Draft'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='a')

    def __str__(self):
        return f"Enrollment {self.id}: Student {self.student.id} in Course {self.course.id}"
    
