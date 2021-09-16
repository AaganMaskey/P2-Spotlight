from django.db import models

# Create your models here.
class creator_fund(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    address1=models.TextField()
    address2=models.TextField()
    zipNo =models.IntegerField()
    cardName= models.TextField()
    cardNum=models.IntegerField()

