from django import forms
# from django.db.models.fields import CharField
from .models import Kafkan

        
class KafkanForm(forms.ModelForm):
    class Meta:
        model = Kafkan
        fields = ['size', 'price', 'color', 'material','name', 'image']
        


# hello world