from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer

def task_list(request):
    # 1. Получаем все задачи из базы данных
    tasks = Task.objects.all()

    # 2. Отдаем их в шаблон (HTML)
    return render(request, 'core/task_list.html', {'tasks': tasks})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at') # Сортируем: новые сверху
    serializer_class = TaskSerializer