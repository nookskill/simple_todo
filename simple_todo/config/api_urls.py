from rest_framework import routers

from simple_todo.apps.tasks.views import TaskViewSet

router = routers.DefaultRouter()

router.register(r'tasks', TaskViewSet, base_name='task')

urlpatterns = [

] + router.urls