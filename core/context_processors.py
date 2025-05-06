# core/context_processors.py
from .models import Configuracao

def configuracoes_site(request):
    """
    Processador de contexto para disponibilizar as configurações do site
    em todos os templates.
    """
    try:
        config = Configuracao.objects.first()
    except:
        config = None
    
    return {'config': config}