from django.db import models
from django.conf import settings
from accounts.models import CustomUser
from django.db.models.deletion import CASCADE
from django.forms import ModelForm





class Kafkan(models.Model):
    size = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    name = models.CharField(max_length=250, blank=True)
    # name each thing differently to distinguish 
    image = models.ImageField(upload_to="./media")
    # description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['image']
    

    
    