# contato/urls.py
from django.urls import path
from . import views

app_name = 'contato'

urlpatterns = [
    path('', views.contato, name='contato'),
    path('newsletter/', views.newsletter_inscricao, name='newsletter_inscricao'),
    path('newsletter/confirmar/<str:token>/', views.newsletter_confirmar, name='newsletter_confirmar'),
    path('newsletter/cancelar/<str:token>/', views.newsletter_cancelar, name='newsletter_cancelar'),
]