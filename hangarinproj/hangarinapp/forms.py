from django import forms
from .models import Task, SubTask, Note, Category, Priority

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name', 'level']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['task', 'title', 'completed']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'flow-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))