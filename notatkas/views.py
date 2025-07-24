from django.shortcuts import render

# Create your views here.
from notatkas import models
from django.views.generic import *

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"
    