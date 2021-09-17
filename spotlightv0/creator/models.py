from django.db import models

# Create your models here.


class creator_Basic(models.Model):
    Creator_Category = (
        ('1','Opt 1'),
        ('2', 'Op 2'),
        ('3', 'Opt 3')
    )
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=1, choices=Creator_Category)
    description=models.TextField()

  

class creator_fund(models.Model):
    amount=models.IntegerField()
   
    
    
