from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title