from django.urls import path
from . import views
urlpatterns = [
	path("tasks/", views.taskList, name="task-list"),
    path("tasks/add", views.addTask, name="add-task"),
    path("", views.index, name="index")
]
