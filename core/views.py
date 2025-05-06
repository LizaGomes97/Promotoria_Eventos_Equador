# core/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from eventos.models import Servico, Portfolio
from .models import SobreNos, Equipe, Depoimento, Banner, FAQ, Parceiro

def home(request):
    """View para a página inicial"""
    banners = Banner.objects.filter(ativo=True).order_by('ordem')
    servicos_destaque = Servico.objects.filter(destaque=True).order_by('ordem')[:4]
    portfolio_destaque = Portfolio.objects.filter(destaque=True).order_by('-data')[:6]
    depoimentos = Depoimento.objects.filter(destaque=True).order_by('-data')[:4]
    parceiros = Parceiro.objects.all().order_by('ordem')
    
    context = {
        'banners': banners,
        'servicos_destaque': servicos_destaque,
        'portfolio_destaque': portfolio_destaque,
        'depoimentos': depoimentos,
        'parceiros': parceiros,
    }
    
    return render(request, 'core/home.html', context)

def sobre_nos(request):
    """View para a página Sobre Nós"""
    sobre = SobreNos.load()  # Usa o método singleton
    equipe = Equipe.objects.all().order_by('ordem')
    depoimentos = Depoimento.objects.all().order_by('-data')
    
    context = {
        'sobre': sobre,
        'equipe': equipe,
        'depoimentos': depoimentos,
    }
    
    return render(request, 'core/sobre_nos.html', context)

def servicos(request):
    """View para a página de serviços"""
    servicos_lista = Servico.objects.all().order_by('ordem')
    
    context = {
        'servicos': servicos_lista,
    }
    
    return render(request, 'core/servicos.html', context)

def servico_detalhe(request, slug):
    """View para detalhes de um serviço"""
    servico = get_object_or_404(Servico, slug=slug)
    servicos_relacionados = Servico.objects.exclude(id=servico.id).order_by('?')[:3]
    
    context = {
        'servico': servico,
        'servicos_relacionados': servicos_relacionados,
    }
    
    return render(request, 'core/servico_detalhe.html', context)

def portfolio(request):
    """View para a página de portfólio"""
    portfolio_lista = Portfolio.objects.all().order_by('-data')
    paginator = Paginator(portfolio_lista, 9)  # 9 projetos por página
    
    page_number = request.GET.get('page')
    portfolio_paginado = paginator.get_page(page_number)
    
    context = {
        'portfolio': portfolio_paginado,
    }
    
    return render(request, 'core/portfolio.html', context)

def portfolio_detalhe(request, slug):
    """View para detalhes de um projeto do portfólio"""
    projeto = get_object_or_404(Portfolio, slug=slug)
    projetos_relacionados = Portfolio.objects.exclude(id=projeto.id).order_by('?')[:3]
    
    context = {
        'projeto': projeto,
        'projetos_relacionados': projetos_relacionados,
    }
    
    return render(request, 'core/portfolio_detalhe.html', context)

def equipe(request):
    """View para a página da equipe"""
    equipe_lista = Equipe.objects.all().order_by('ordem')
    
    context = {
        'equipe': equipe_lista,
    }
    
    return render(request, 'core/equipe.html', context)

def faq(request):
    """View para a página de perguntas frequentes"""
    perguntas = FAQ.objects.all().order_by('ordem')
    
    context = {
        'perguntas': perguntas,
    }
    
    return render(request, 'core/faq.html', context)