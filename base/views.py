from django.shortcuts import render
from django.views import generic

from .models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'base/task_detail.html'


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'base/task_create_form.html'
    fields = '__all__'


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = 'base/task_update_form.html'
    fields = '__all__'