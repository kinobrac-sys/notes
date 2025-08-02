
from dataclasses import field
from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = Task
        fields = ['title', 'desc', 'status', 'prior', 'due']
        widgets = {
            'due': forms.DateInput(attrs={'type': 'date'}),
        }

class TaskFilterForm(forms.Form):
    STATUS_CHOISES = [
        ("To Do", "To Do"),
        ("In Progression", "In progression"),
        ("Done", "Done")
    ]

    PRIORITY = [    
        ("low",'low'),
        ("med", "Medium"),
        ('high', 'High'),
        ('2high', 'PIZDA HIGH')
    ]
    status = forms.CharField(choices=STATUS_CHOISES, label='Status')
    priority = forms.CharField(choices=PRIORITY, label='Priority')
    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})