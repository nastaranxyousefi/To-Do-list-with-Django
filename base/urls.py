from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('task-create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),

    
]
