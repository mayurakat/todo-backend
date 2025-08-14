from django.test import TestCase
from .models import Task
from .openai_utils import generate_task, set_priority

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(description="Test Task", priority=1)

    def test_task_creation(self):
        self.assertEqual(self.task.description, "Test Task")
        self.assertEqual(self.task.priority, 1)

class OpenAIUtilsTest(TestCase):
    def test_generate_task(self):
        task_description = generate_task("Write a blog post about AI.")
        self.assertIsInstance(task_description, str)

    def test_set_priority(self):
        priority = set_priority("This task is urgent.")
        self.assertIn(priority, [1, 2, 3])  # Assuming 1 is high, 2 is medium, 3 is low