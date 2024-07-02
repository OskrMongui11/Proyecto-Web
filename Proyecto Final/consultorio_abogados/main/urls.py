from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('abogado/', views.abogado_home, name='abogado_home'),
    path('cliente/', views.cliente_home, name='cliente_home'),
    path('crear_proceso/', views.crear_proceso, name='crear_proceso'),
    path('ver_procesos/', views.ver_procesos, name='ver_procesos'),
]
