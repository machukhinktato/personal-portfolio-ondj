from django import forms
from django.forms import ModelForm
from .models import ToDoModel


class ToDoForm(ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['title', 'description', 'high_priority']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            # 'high_priority': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

    # def  clean_