from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tareas_list, name='Tareas_list'),
]