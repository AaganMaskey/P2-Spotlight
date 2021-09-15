from django.db import models

# Create your models here.

class creator_Basic(models.Model):
    Category_Choices = (
    ('art','ART'),
    ('design', 'DESIGN'),
    ('fashion','FASHION'),
    ('food','FOOD'),
    ('games','GAME'),
    ('technology','TECHNOLOGY'),
    ('photography','PHOTOGRAPHY'),)
    category = models.CharField(max_length=15, choices= Category_Choices, default='technology')
    title=models.CharField(max_length=50)
    description=models.TextField()
    email = models.EmailField()


class creator_fund(models.Model):
    amount=models.IntegerField()
   
    
    
