from django.test import TestCase
from model_mommy import mommy
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from simple_todo.apps.tasks.models import Task


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.task = mommy.make(
            Task,
            subject='Test',
            content='This is test',
            status=Task.PENDING
        )

    def test_update_status(self):
        self.assertEqual(self.task.status, Task.PENDING)
        self.task.status = Task.DONE
        self.task.save()
        self.assertEqual(self.task.status, Task.DONE)

    def test_edit_task(self):
        subject = 'Update Subject'
        content = 'Update Content'
        status = Task.DONE
        self.task.subject = subject
        self.task.content = content
        self.task.status = status
        self.task.save()
        self.assertEqual(self.task.subject, subject)
        self.assertEqual(self.task.content, content)
        self.assertEqual(self.task.status, status)


class TaskViewSetTestCase(APITestCase):

    def test_blog_api_create(self):
        url = reverse('api:task-list')
        data = {'subject': 'Test Subject', 'content': 'This is content', 'status': Task.PENDING}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
