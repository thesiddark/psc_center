from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def deleted(self):
        return super().get_queryset().filter(is_deleted=True)

    def all_objects(self):
        return super().get_queryset()

class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_by= models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True,blank=True, related_name='%(class)s_created_by')
    updated_by= models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True,blank=True, related_name='%(class)s_updated_by')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


    

    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    class Meta:
        abstract = True
        ordering = ['-created_date']

    def soft_delete(self):
        self.is_deleted = True
        self.save(update_fields=['is_deleted'])

    def restore(self):
        self.is_deleted = False
        self.save(update_fields=['is_deleted'])

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.pk})"