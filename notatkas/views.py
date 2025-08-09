from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from . import forms
from django.views.generic import *
from .models import Task, Comment

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "notatkas/task_list.html"   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.TaskFilterForm()
        return context

    def get_queryset(self):
        queryset =  Task.objects.filter(creator=self.request.user)
        status = self.request.GET.get('status', "")
        priority = self.request.GET.get('priority', "")

        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(prior=priority)

        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = forms.TaskForm
    template_name = "notatkas/task-create.html"
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "notatkas/task-update.html"
    success_url = reverse_lazy('task-list')
    form_class = forms.TaskForm

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "notatkas/task-delete.html"
    success_url = reverse_lazy('task-list')