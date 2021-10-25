from django.db import models
from django.conf import settings
from django.forms import ModelForm




class Kafkan(models.Model):
    size = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    name = models.CharField(max_length=250, default="Kafkan")
    # name each thing differently to distinguish 
    image = models.ImageField()
    # description = models.TextField()
    
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['image']
    

    
    