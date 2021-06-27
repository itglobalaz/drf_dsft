from rest_framework import serializers
from src.main.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'author',
            'title',
            'img',
            'description',
            'created_at',
            'updated_at',
            'author',
            'users'
        )
