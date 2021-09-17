from django.db import models

# Create your models here.


class creator_Basic(models.Model):
    Creator_Category = (
        ('1','Art'),
        ('2', 'Technology'),
        ('3', 'Fasion'),
        ('4', 'Food'),
        ('5', 'Photography'),
        ('6', 'Others')
    )
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=1, choices=Creator_Category)
    description=models.TextField()
    image = models.ImageField(upload_to='static/img')


  

class creator_fund(models.Model):
    amount=models.IntegerField()
   
    
    
