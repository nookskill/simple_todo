from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from simple_todo.apps.tasks.models import Task
from simple_todo.apps.tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('status', )
