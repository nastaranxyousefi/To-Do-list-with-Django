from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/Login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


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


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'base/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')
