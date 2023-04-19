from django.urls import path
from coder import views

# app_name = 'coder'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prueba-render/', views.prueba_render, name='prueba_render'),
]