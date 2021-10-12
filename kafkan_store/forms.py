from django import forms
from django.db.models.fields import CharField
from django.forms.models import inlineformset_factory
from .models import Kafkan

        
class KafkanForm(forms.ModelForm):
    class Meta:
        model = Kafkan
        fields = ('size', 'price', 'color', 'material',)


# KafkanFormSet = forms.inlineformset_factory(Kafkan, form = KafkanForm, extra=1)
        
        
class KafkanForm(forms.Form):
    size = forms.CharField(max_length=40)
    price = forms.DecimalField()
    color= forms.TextInput()
    material = forms.TextInput()
    
class OrderByForm(forms.Form):
    order = CharField(max_length=120)