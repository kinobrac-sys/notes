

from django.contrib import admin
from django.urls import path
from notatkas import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name="task-list"),
    path('create/', views.TaskCreateView.as_view(), name="task-create"),
]
