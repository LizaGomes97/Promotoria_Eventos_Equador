# eventos/urls.py
from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.eventos_lista, name='eventos_lista'),
    path('tipo/<slug:slug>/', views.eventos_por_tipo, name='eventos_por_tipo'),
    path('<slug:slug>/', views.evento_detalhe, name='evento_detalhe'),
    path('calendario/', views.calendario_eventos, name='calendario_eventos'),
]