from django.db import models
from students.models import Enrollment


# Create your models here.

from utility.models import BaseModel

class Assignment(BaseModel):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('staff.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} (course: {self.course.title})"
    
    
class Submission(BaseModel):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('late', 'Late'),
        ('graded', 'Graded'),
    ]

    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    file_url = models.CharField(max_length=255, blank=True, null=True)
    submitted_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return f"Submission {self.id}: for assignment {self.assignment.title} by {self.student.first_name}"


class SubmissionGrade(BaseModel):
    submission = models.OneToOneField('Submission', on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    graded_by = models.ForeignKey('staff.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Grade for {self.grade}: Submission {self.submission.id}"
