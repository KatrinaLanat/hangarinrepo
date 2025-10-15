from django.contrib import admin
from .models import Task, SubTask, Note, Category, Priority

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority', 'category', 'created_at')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description')
    
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('title',)
    
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
