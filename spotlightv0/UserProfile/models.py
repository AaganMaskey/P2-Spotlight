from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class profile_Basic(models.Model):

    User = models.CharField(max_length=25)
    Email = models.EmailField(max_length=25)
    Phone = models.IntegerField(default='0')
    Address = models.CharField(max_length=25)
    Funded = models.IntegerField(default='0')
    Projects = models.CharField(max_length=100)
    