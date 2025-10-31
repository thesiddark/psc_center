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