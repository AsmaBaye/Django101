from django.shortcuts import render

# Create your views here.
mytasklist = ['5AM', '30X', 'RJS and VSC']
def taskList(request):
    return render(request, 'tasks/lists.html', 
               {"tasks": mytasklist})
 
def addTask(request):
 	return render(request, 'tasks/add.html')

def index(request):
	return render(request, 'tasks/index.html')