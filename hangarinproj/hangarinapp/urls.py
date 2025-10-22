from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.HomePageView.as_view(), name='home'),

    # Tasks
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/add/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    # SubTasks
    path('subtasks/', views.SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add/', views.SubTaskCreateView.as_view(), name='subtask-create'),
    path('subtasks/<int:pk>/edit/', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtasks/<int:pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask-delete'),

    # Notes
    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/add/', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),

    # Categories
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Priorities
    path('priorities/', views.PriorityListView.as_view(), name='priority-list'),
    path('priorities/add/', views.PriorityCreateView.as_view(), name='priority-create'),
    path('priorities/<int:pk>/edit/', views.PriorityUpdateView.as_view(), name='priority-update'),
    path('priorities/<int:pk>/delete/', views.PriorityDeleteView.as_view(), name='priority-delete'),
]
