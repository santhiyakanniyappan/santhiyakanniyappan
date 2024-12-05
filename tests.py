from django.test import TestCase
from rest_framework.test import APIClient
from .models import TodoItem

class TodoItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_data = {
            "title": "Test Task",
            "description": "This is a test task",
            "status": "OPEN"
        }

    def test_create_todo(self):
        response = self.client.post('/api/create/', self.todo_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_list_todos(self):
        TodoItem.objects.create(**self.todo_data)
        response = self.client.get('/api/list/')
        self.assertEqual(response.status_code, 200)
