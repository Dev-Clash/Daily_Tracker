from django.urls import path
from .views import TaskListCreateView, TaskUpdateDeleteView

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('<int:pk>/', TaskUpdateDeleteView.as_view()),
]
