from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

User = settings.AUTH_USER_MODEL 

class ObjectViewd(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    ip_address = models.CharField(max_length=12,blank=True,null=True)
    content_type  = models.ForeignKey(ContentType,on_delete=models.SET_NULL,null=True,blank=True)
    object_id =     models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed  on %s" %(self.content_object,self.timestamp)
    
    class Mata:
        ordering = ['-timestamp']
        verbose_name = 'object_viewed'
        verbose_name_plural = 'abjects viewed'