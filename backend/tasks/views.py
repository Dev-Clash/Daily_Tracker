from django.contrib.auth.models import Permission
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from rest_framework import permissions
from .serializers import TaskSerializer

# Create your views here.


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer


class TaskUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerializer
