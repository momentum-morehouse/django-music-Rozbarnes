from django import forms
from .models import Album, Detail

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'released',
            'image_url',
            
        ]
        widgets = {
        'released': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class DetailForm(forms.ModelForm):
  class Meta:
    model = Detail
    fields = ['text']