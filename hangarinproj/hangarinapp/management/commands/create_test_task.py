from django.core.management.base import BaseCommand
from django.utils import timezone
from hangarinapp.models import Task, SubTask, Note, Category, Priority

class Command(BaseCommand):
    help = "Create one Task with a SubTask and a Note for testing inlines"

    def handle(self, *args, **kwargs):
        category = Category.objects.first()
        priority = Priority.objects.first()

        if not category or not priority:
            self.stdout.write(self.style.WARNING(
                "Please add at least one Category and one Priority in admin first."
            ))
            return

        task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            status="Pending",
            deadline=timezone.now(),
            priority=priority,
            category=category
        )

        SubTask.objects.create(
            task=task,
            title="Test SubTask",
            status="Pending"
        )

        Note.objects.create(
            task=task,
            content="This is a test note"
        )

        self.stdout.write(self.style.SUCCESS(
            "Test Task with SubTask and Note created successfully!"
        ))
