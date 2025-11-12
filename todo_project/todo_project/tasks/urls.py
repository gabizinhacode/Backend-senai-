from django.urls import path
from .views import listar_tasks, criar_task
urlpatterns = [
    path('', listar_tasks, name='listar_tasks'),
    path('criar/', criar_task, name='criar_task'),
]

