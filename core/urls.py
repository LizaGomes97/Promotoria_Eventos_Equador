# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('servicos/', views.servicos, name='servicos'),
    path('servico/<slug:slug>/', views.servico_detalhe, name='servico_detalhe'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', views.portfolio_detalhe, name='portfolio_detalhe'),
    path('equipe/', views.equipe, name='equipe'),
    path('perguntas-frequentes/', views.faq, name='faq'),
]



