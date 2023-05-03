from django.contrib.auth.views import LogoutView
from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]