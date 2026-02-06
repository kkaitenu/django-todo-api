from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer
from django.shortcuts import render, get_object_or_404

def task_list(request):
    # 1. Получаем все задачи из базы данных
    tasks = Task.objects.all()

    # 2. Отдаем их в шаблон (HTML)
    return render(request, 'core/task_list.html', {'tasks': tasks})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at') # Сортируем: новые сверху
    serializer_class = TaskSerializer

def about(request):
    return render(request, 'core/about.html')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'core/task_detail.html', {'task': task})