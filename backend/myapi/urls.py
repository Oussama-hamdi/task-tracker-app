from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks, name='get_tasks'),  # GET endpoint
    path('tasks/add/', views.add_task, name='add_task'),  # POST endpoint
]
