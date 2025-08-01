from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from notatkas import models
from django.views.generic import *

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "notatkas/task_list.html"



class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    fields = ['title', 'desc', 'status', 'prior', 'due']
    template_name = "notatkas/task-create.html"
    success_url = reverse_lazy('task-list')