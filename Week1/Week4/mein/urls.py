from django.urls import path, include 
from . import views

urlpatterns = [
    path('Book/', views.book),
    path('Author/', views.author),
    path('Publisher/', views.publisher)
]

