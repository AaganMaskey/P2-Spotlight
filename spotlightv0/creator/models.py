from django.db import models

# Create your models here.


class creator_Basic(models.Model):
  
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='static/img')


  

class creator_fund(models.Model):
    amount=models.IntegerField()
   
    
    
