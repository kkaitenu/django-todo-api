from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import task_list, TaskViewSet, about, task_detail # <-- Добавь

# Создаем роутер для API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Главная страница (твоя HTML красивая)
    path('', task_list, name='home'),

    # Адреса для API (все пути начнутся с api/)
    path('api/', include(router.urls)),

    path('about/', about, name='about'),

    path('task/<int:pk>/', task_detail, name='task_detail'),
]

