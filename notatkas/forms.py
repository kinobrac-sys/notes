
from dataclasses import field
from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control my-input'})
    
    class Meta:
        model = Task
        fields = ['title', 'desc', 'status', 'prior', 'due']
        widgets = {
            'due': forms.DateInput(attrs={'type': 'date'}),
        }

class TaskFilterForm(forms.Form):
    STATUS_CHOISES = [
        ('', "all"),
        ("To Do", "To Do"),
        ("In Progression", "In progression"),
        ("Done", "Done")
    ]

    PRIORITY = [
        ("", "All"),
        ("low",'low'),
        ("med", "Medium"),
        ('high', 'High'),
        ('2high', 'PIZDA HIGH')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOISES, label='Status', required=False)
    priority = forms.ChoiceField(choices=PRIORITY, label='Priority', required=False)
    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})