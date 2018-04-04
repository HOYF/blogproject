# -*- conding:utf-8 -*-
from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        widgets = {'name':forms.TextInput(attrs={'placeholder': 'Name'}),
                   'email':forms.TextInput(attrs={'placeholder': 'Email'}),
                   'subject':forms.TextInput(attrs={'placeholder':'Subject'}),
                   'message': forms.Textarea(
                attrs={'placeholder': 'Enter Your Message'})}
        fields = ['name', 'email', 'subject', 'message']