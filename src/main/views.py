from django.core.mail import send_mail
from rest_framework import generics, permissions

from config import settings
from src.main.models import Task
from src.main.serializers import TaskSerializer
from src.main.permissions import IsAuthorOrReadOnly

""" Список заданий """


class Task_List(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


""" Создать задание """


class New_Task(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    """ Отправка почты исполнителям после добавления нового таска """

    def _send_notifications(self, serializer):
        title = serializer.validated_data['title']
        author = self.request.user
        description = serializer.validated_data['description']
        recipient_list = [users.email for users in serializer.validated_data['users']]

        subject = f"New task: {title}"
        message = f"Hello, you have a new task promoted by {author} with following content:\n\n\t {description}"

        return send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL,
                         recipient_list=recipient_list)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        self._send_notifications(serializer)
        return serializer.save()


""" Просмотр заданий """


class Task_Detail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


""" Редактировать задание """


class Task_Edit(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]


""" Удалить задание """


class Task_Delete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
