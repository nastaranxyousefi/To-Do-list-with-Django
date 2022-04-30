from django.urls import path
from django.contrib.auth.views import LogoutView 

from . import views

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.SignUpPage.as_view(), name='signup'),
    
    path('', views.TaskListView.as_view(), name='tasks'),
    path('task-create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),

    
]
