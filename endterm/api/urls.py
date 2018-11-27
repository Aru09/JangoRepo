from django.urls import path
from api import views

urlpatterns=[
    path('achievements/', views.ahievements_list),
    path('persons/', views.persons_list)

]