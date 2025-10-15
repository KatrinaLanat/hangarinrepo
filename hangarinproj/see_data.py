import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarinproj.settings')
django.setup()

from hangarinapp.models import Category, Priority, Task

# Clear existing data
Category.objects.all().delete()
Priority.objects.all().delete()
Task.objects.all().delete()

# Create sample categories
work = Category.objects.create(name="Work", description="Work-related tasks")
personal = Category.objects.create(name="Personal", description="Personal errands")

# Create sample priorities
high = Priority.objects.create(name="High", level=1)
medium = Priority.objects.create(name="Medium", level=2)
low = Priority.objects.create(name="Low", level=3)

# Create sample task
task = Task.objects.create(
    title="Finish Hangarin Project",
    description="Complete all Django components and test.",
    deadline="2025-10-20",
    status="in_progress",
    category=work,
    priority=high
)

print("✅ Sample data successfully added!")
print(f"Task: {task.title}, Category: {task.category.name}, Priority: {task.priority.name}")
