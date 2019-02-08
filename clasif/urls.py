from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tareas_list, name='Tareas_list'),
    path('Tareas/<int:pk>/', views.Tareas_detalle, name='Tareas_detalle'),
    path('Tareas/new', views.Tareas_new, name='Tareas_new'),
    path('Tareas/<int:pk>/edit/', views.Tareas_edit, name='Tareas_edit'),
]