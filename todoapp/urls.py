from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('index/', views.index),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create_task/', views.createTask),
    path('blog/', views.blog)
]
