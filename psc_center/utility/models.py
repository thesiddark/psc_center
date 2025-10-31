from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract = True
    created_by= models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True,blank=True, related_name='%(class)s_created_by')
    updated_by= models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True,blank=True, related_name='%(class)s_updated_by')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


    

    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()
        
    class Meta:
        abstract = True