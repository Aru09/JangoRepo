from django import forms
from .models import Task

class  TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['task_name' ,  'due_on', 'owner', 'mark', 'task_list']
		widgets = { 
        	'due_on': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        	'task_name' : forms.TextInput(attrs={'class': 'form-control'}),
        	'owner' : forms.TextInput(attrs={'class': 'form-control'}),
        	'task_list' : forms.TextInput(attrs={'class': 'form-control'}),
        	 


        }
