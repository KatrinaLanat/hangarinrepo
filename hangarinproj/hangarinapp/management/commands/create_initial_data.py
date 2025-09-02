from django.core.management.base import BaseCommand
from faker import Faker
from hangarinapp.models import Task, SubTask, Note, Priority, Category
from django.utils import timezone
import random

fake = Faker()

class Command(BaseCommand):
    help = "Populate tasks, subtasks, and notes with fake data"

    def handle(self, *args, **kwargs):
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        for _ in range(10):  # Create 10 tasks
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=random.choice(priorities),
                category=random.choice(categories)
            )

            # Create 1-3 subtasks
            for _ in range(random.randint(1, 3)):
                SubTask.objects.create(
                    task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"])
                )

            # Create 1-2 notes
            for _ in range(random.randint(1, 2)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2)
                )

        self.stdout.write(self.style.SUCCESS("Fake data populated successfully!"))
