from django.urls import path, include
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
]
