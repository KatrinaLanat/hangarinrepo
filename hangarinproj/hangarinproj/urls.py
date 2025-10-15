from django.contrib import admin
from django.urls import path
from hangarinapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.HomePageView.as_view(), name='home'),

    # Task URLs
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    # SubTask URLs
    path('subtasks/', views.SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add/', views.SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtasks/<int:pk>/edit/', views.SubTaskUpdateView.as_view(), name='subtask-edit'),
    path('subtasks/<int:pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask-delete'),

    # Note URLs
    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/add/', views.NoteCreateView.as_view(), name='note-add'),
    path('notes/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note-edit'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),
]
