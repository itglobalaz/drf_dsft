from django.contrib import admin

from src.main.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author',)
    list_filter = ('users', 'created_at',)
    date_hierarchy = 'created_at'

    """ Сохранения юзера при добавлений заданий """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)