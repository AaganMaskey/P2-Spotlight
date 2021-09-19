from django.db import models
from django.utils.timezone import now



# Create your models here.


class creator_Basic(models.Model):
  
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='media/static/img')
    FundingGoal=models.IntegerField(default='0')
    TargetLaunchDate = models.DateField(default= now, blank=True)

   
    
    
