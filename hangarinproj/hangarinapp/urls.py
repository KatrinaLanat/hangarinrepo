from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # TASKS
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/add/', views.task_create, name='task-create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task-update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task-delete'),

    # SUBTASKS
    path('subtasks/', views.subtask_list, name='subtask-list'),
    path('subtasks/add/', views.subtask_create, name='subtask-create'),
    path('subtasks/<int:pk>/edit/', views.subtask_update, name='subtask-update'),
    path('subtasks/<int:pk>/delete/', views.subtask_delete, name='subtask-delete'),

    # NOTES
    path('notes/', views.note_list, name='note-list'),
    path('notes/add/', views.note_create, name='note-create'),
    path('notes/<int:pk>/edit/', views.note_update, name='note-update'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note-delete'),

    # CATEGORIES
    path('categories/', views.category_list, name='category-list'),
    path('categories/add/', views.category_create, name='category-create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category-update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category-delete'),

    # PRIORITIES
    path('priorities/', views.priority_list, name='priority-list'),
    path('priorities/add/', views.priority_create, name='priority-create'),
    path('priorities/<int:pk>/edit/', views.priority_update, name='priority-update'),
    path('priorities/<int:pk>/delete/', views.priority_delete, name='priority-delete'),
]
