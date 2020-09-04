from django import forms
from .models import Notes

class Noteform(forms.ModelForm):
    class Meta:
        model=Notes
        fields=[
            'title',
            'image',
            'url',
        ]