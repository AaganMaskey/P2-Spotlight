from django.db import models
from django.utils.timezone import now

# Create your models here.


class investor_fund(models.Model):
    username = models.CharField(max_length=25, blank=True)
    userid = models.CharField(max_length=25, blank=True)
    projectid = models.CharField(max_length=25, blank=True)
    pledgeAmount = models.IntegerField(default='0')
    created_at = models.DateField(default=now, blank=True)
    updated_at = models.DateField(default=now, blank=True)
