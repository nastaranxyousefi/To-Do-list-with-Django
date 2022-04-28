from django.shortcuts import render
from django.views import generic

from .models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'
