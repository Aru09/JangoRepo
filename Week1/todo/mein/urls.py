from django.urls import path, include 
from . import views

urlpatterns = [
    path('todo_list/', views.todo_list),
    path('completed_todo_list/', views.completed_todo_list)
]

