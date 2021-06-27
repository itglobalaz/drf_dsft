from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE,
                               related_name="tasks_author", editable=False)
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    img = models.ImageField(upload_to='images/', verbose_name="Фото", blank=True)
    description = models.TextField(verbose_name="Описание", max_length=35000)
    users = models.ManyToManyField(User, verbose_name="Выбор исполнителя", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "1. Задачи"

    def __str__(self):
        return self.title
