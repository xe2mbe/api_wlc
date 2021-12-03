from django.db import models

# Create your models here.

class guestUser(models.Model):
    netuser = models.CharField(max_length=40)
    netpass = models.CharField(max_length=40)
    wlanID = models.IntegerField(max_length=1)
    lifetime = models.IntegerField(max_length=7)
    description = models.CharField(max_length=40)

    class Meta:
        ordering = ['netuser']    
