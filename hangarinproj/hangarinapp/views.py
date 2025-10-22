from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm

# ---------------------------
# ROOT REDIRECT VIEW
# ---------------------------
def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')  # Make sure 'home' is the name of your HomePageView URL
    else:
        return redirect('account_login')  # Allauth login page

# ---------------------------
# HOME PAGE
# ---------------------------
class HomePageView(LoginRequiredMixin, View):
    login_url = 'account_login'
    redirect_field_name = 'next'

    def get(self, request):
        total_tasks = Task.objects.count()
        completed_tasks = Task.objects.filter(status="completed").count()
        pending_tasks = Task.objects.filter(status="pending").count()
        in_progress_tasks = Task.objects.filter(status="in_progress").count()

        context = {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'in_progress_tasks': in_progress_tasks,
        }
        return render(request, 'home.html', context)

# ---------------------------
# TASK VIEWS
# ---------------------------
class TaskListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'account_login'
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task-list')

# ---------------------------
# SUBTASK VIEWS
# ---------------------------
class SubTaskListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = SubTask
    template_name = 'subtask_list.html'
    context_object_name = 'subtasks'

class SubTaskCreateView(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'account_login'
    model = SubTask
    template_name = 'subtask_delete.html'
    success_url = reverse_lazy('subtask-list')

    
# ---------------------------
# NOTE VIEWS
# ---------------------------
class NoteListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'

class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'account_login'
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note-list')



# ---------------------------
# CATEGORY VIEWS
# ---------------------------
class CategoryListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'account_login'
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category-list')


# ---------------------------
# PRIORITY VIEWS
# ---------------------------
class PriorityListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = Priority
    template_name = 'priority_list.html'
    context_object_name = 'priorities'

class PriorityCreateView(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'account_login'
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'account_login'
    model = Priority
    template_name = 'priority_delete.html'
    success_url = reverse_lazy('priority-list')
