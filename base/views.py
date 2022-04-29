from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/Login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'base/task_detail.html'


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = 'base/task_create_form.html'
    fields = ['title', 'description', 'complete',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = 'base/task_update_form.html'
    fields = '__all__'


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'base/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')
