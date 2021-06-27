from django.urls import path
from src.main import views

urlpatterns = [
    path('tasks/', views.Task_List.as_view()),
    path('task/detail/<int:pk>/', views.Task_Detail.as_view()),
    path('task/edit/<int:pk>/', views.Task_Edit.as_view()),
    path('task/create/', views.New_Task.as_view()),
    path('task/delete/<int:pk>/', views.Task_Delete.as_view())
]