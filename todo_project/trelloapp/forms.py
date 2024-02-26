from django import forms
from .models import Tasks

class TaskFormsOld(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=255, widget=forms.Textarea)
    created_at = forms.DateField()
    due_date = forms.DateField()

class TaskForms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'priority', 'due_date']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

