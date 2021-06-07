from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="1st todo", body="1st body here")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.title}"
        self.assertEqual(expected_object_name, "1st todo")

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.body}"
        self.assertEqual(expected_object_name, "1st body here")
