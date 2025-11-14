from django.db import models
from students.models import Enrollment

from utility.models import BaseModel
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Course(BaseModel):
    STATUS_CHOICES = (
        ('a', 'Archived'),
        ('p', 'Published'),
        ('d', 'Draft'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='d') 

    def __str__(self):
        return f"{self.id} : {self.title}"

class CourseTeacher(BaseModel):
    STATUS_CHOICES = (
        ("a", "Active"),
        ("i", "Inactive"),
    )

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_teachers')
    teacher = models.ForeignKey('staff.Teacher', on_delete=models.CASCADE, related_name='teacher_courses')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')

    def __str__(self):
        return f"{self.course.title} - {self.teacher.first_name}"
    
class Material(BaseModel):
    TYPE_CHOICES = (
        ("document", "Document"),
        ("video", "Video"),
        ("link", "Link"),
        ("slides", "Slides"),
    )
    STATUS_CHOICES = (
        ("a", "Active"),
        ("i", "Inactive"),
    )

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='materials')
    teacher = models.ForeignKey('staff.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    file_url = models.CharField(max_length=255, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="document")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="a")

    def __str__(self):
        return f"{self.title} ({self.type})"


@receiver(models.signals.pre_save, sender=Course)
def course_pree_save(sender, instance, **kwargs):
    print(f"signal workeddddd...: {instance.title}")
    instance.description="dessscccc"


@receiver(models.signals.post_save, sender=Course)
def course_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"curse created :-Post Save signal worked...: {instance.title}")
    else:
        print(f"course updated :-Post Save signal worked...: {instance.title}")