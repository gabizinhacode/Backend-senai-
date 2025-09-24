from django.urls import path
from . import views

urlpatterns = [
    path('pizza-do-dia/', views.pizza_do_dia, name='pizza_do_dia'),
    path('promocoes/', views.promocoes, name='promocoes'),
]
