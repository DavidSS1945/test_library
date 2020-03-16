from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    edithorial = models.ForeignKey('Edithorial',null=True,blank=True, on_delete = models.CASCADE)  
    
    
class Edithorial(models.Model):
    name  = models.CharField(max_length=250)

