from django.urls import path, include ,re_path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('todos/', views.todos, name='todos' ),
    path('subject/', views.subject, name='subject' ),
    path('todos/add/', views.add, name = 'add' ),
    re_path(r'todos/(\d+)/delete/$', views.delete, name= 'delete'),

    re_path(r'^todos/(\d+)/completed/$', views.completed_todos, name='completed_todos'),
]    



