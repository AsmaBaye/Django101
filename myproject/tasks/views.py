from django.shortcuts import render
from django import forms

# Create your views here.
mytasklist = ['5AM', '30X', 'RJS and VSC']

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
def taskList(request):
    return render(request, 'tasks/lists.html', 
               {"tasks": mytasklist})
 
def addTask(request):
 	return render(request, 'tasks/add.html',
                {"form": NewTaskForm()})

def index(request):
	return render(request, 'tasks/index.html')
