# eventos/views.py

import json

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime

from .models import Evento, TipoEvento

def eventos_lista(request):
    """View para listar todos os eventos"""
    # Filtros
    tipo_id = request.GET.get('tipo')
    status = request.GET.get('status')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    busca = request.GET.get('busca')
    
    # Query base
    eventos_lista = Evento.objects.all()
    
    # Aplicar filtros se fornecidos
    if tipo_id:
        eventos_lista = eventos_lista.filter(tipo_id=tipo_id)
    
    if status:
        eventos_lista = eventos_lista.filter(status=status)
    
    if data_inicio:
        try:
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
            eventos_lista = eventos_lista.filter(data_inicio__gte=data_inicio)
        except ValueError:
            pass
    
    if data_fim:
        try:
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
            eventos_lista = eventos_lista.filter(data_inicio__lte=data_fim)
        except ValueError:
            pass
    
    if busca:
        eventos_lista = eventos_lista.filter(
            Q(nome__icontains=busca) | 
            Q(descricao_curta__icontains=busca) | 
            Q(descricao__icontains=busca) |
            Q(local__icontains=busca) |
            Q(cidade__icontains=busca)
        )
    
    # Ordenação padrão
    eventos_lista = eventos_lista.order_by('-data_inicio')
    
    # Paginação
    paginator = Paginator(eventos_lista, 9)  # 9 eventos por página
    page_number = request.GET.get('page')
    eventos_paginados = paginator.get_page(page_number)
    
    # Tipos de eventos para o filtro
    tipos_evento = TipoEvento.objects.all()
    
    context = {
        'eventos': eventos_paginados,
        'tipos_evento': tipos_evento,
        'filtros': {
            'tipo_id': tipo_id,
            'status': status,
            'data_inicio': data_inicio,
            'data_fim': data_fim,
            'busca': busca,
        }
    }
    
    return render(request, 'eventos/eventos_lista.html', context)

def eventos_por_tipo(request, slug):
    """View para listar eventos por tipo"""
    tipo = get_object_or_404(TipoEvento, slug=slug)
    eventos_lista = Evento.objects.filter(tipo=tipo).order_by('-data_inicio')
    
    # Paginação
    paginator = Paginator(eventos_lista, 9)  # 9 eventos por página
    page_number = request.GET.get('page')
    eventos_paginados = paginator.get_page(page_number)
    
    context = {
        'tipo': tipo,
        'eventos': eventos_paginados,
    }
    
    return render(request, 'eventos/eventos_por_tipo.html', context)

def evento_detalhe(request, slug):
    """View para detalhes de um evento"""
    evento = get_object_or_404(Evento, slug=slug)
    eventos_relacionados = Evento.objects.filter(tipo=evento.tipo).exclude(id=evento.id).order_by('-data_inicio')[:3]
    
    context = {
        'evento': evento,
        'eventos_relacionados': eventos_relacionados,
    }
    
    return render(request, 'eventos/evento_detalhe.html', context)

def calendario_eventos(request):
    """View para o calendário de eventos"""
    # Obter todos os eventos para o calendário (formato JSON)
    eventos = Evento.objects.all()
    
    # Converter eventos para o formato esperado pelo FullCalendar
    eventos_calendario = []
    for evento in eventos:
        eventos_calendario.append({
            'id': evento.id,
            'title': evento.nome,
            'start': evento.data_inicio.isoformat(),
            'end': evento.data_fim.isoformat(),
            'url': f'/eventos/{evento.slug}/',
            'className': f'evento-{evento.status}',
            'description': evento.descricao_curta
        })
    
    eventos_json = json.dumps(eventos_calendario)
    
    return render(request, 'eventos/calendario_eventos.html', {
        'eventos_json': eventos_json,
        'tipos_evento': TipoEvento.objects.all(),
    })