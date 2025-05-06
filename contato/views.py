# contato/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
import uuid
import hashlib

from .models import Contato, Newsletter
from .forms import ContatoForm, NewsletterForm

def contato(request):
    """View para a página de contato"""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Salvar o formulário
            contato = form.save()
            
            # Enviar e-mail de notificação para administrador
            assunto = f"Nova mensagem de contato: {contato.get_assunto_display()}"
            mensagem = f"""
            Nova mensagem de contato recebida:
            
            Nome: {contato.nome}
            Email: {contato.email}
            Telefone: {contato.telefone}
            Assunto: {contato.get_assunto_display()}
            Mensagem: {contato.mensagem}
            
            Data de envio: {contato.data_envio}
            """
            
            try:
                send_mail(
                    assunto,
                    mensagem,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            except Exception as e:
                messages.warning(request, 'Sua mensagem foi recebida, mas houve um problema ao enviar notificação. Entraremos em contato em breve.')
            
            return redirect('contato:contato')
    else:
        form = ContatoForm()
    
    # Formulário de newsletter no rodapé
    newsletter_form = NewsletterForm()
    
    context = {
        'form': form,
        'newsletter_form': newsletter_form,
    }
    
    return render(request, 'contato/contato.html', context)

def newsletter_inscricao(request):
    """View para inscrição na newsletter"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nome = form.cleaned_data.get('nome', '')
            
            # Verificar se o e-mail já está cadastrado
            if Newsletter.objects.filter(email=email).exists():
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'status': 'info', 'message': 'Este e-mail já está inscrito em nossa newsletter.'})
                else:
                    messages.info(request, 'Este e-mail já está inscrito em nossa newsletter.')
            else:
                # Criar nova inscrição
                newsletter = Newsletter(email=email, nome=nome)
                newsletter.save()
                
                # Gerar token para confirmação
                token = hashlib.sha256(f"{email}{uuid.uuid4()}".encode()).hexdigest()
                
                # Enviar e-mail de confirmação
                assunto = "Confirme sua inscrição em nossa newsletter"
                confirmar_url = request.build_absolute_uri(reverse('contato:newsletter_confirmar', args=[token]))
                cancelar_url = request.build_absolute_uri(reverse('contato:newsletter_cancelar', args=[token]))
                
                mensagem = f"""
                Olá {nome or email},
                
                Obrigado por se inscrever em nossa newsletter!
                
                Para confirmar sua inscrição, clique no link abaixo:
                {confirmar_url}
                
                Se você não solicitou esta inscrição, simplesmente ignore este e-mail ou clique para cancelar:
                {cancelar_url}
                
                Atenciosamente,
                Equipe Equador Eventos
                """
                
                try:
                    send_mail(
                        assunto,
                        mensagem,
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )
                    
                    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                        return JsonResponse({'status': 'success', 'message': 'Inscrição realizada com sucesso! Verifique seu e-mail para confirmar.'})
                    else:
                        messages.success(request, 'Inscrição realizada com sucesso! Verifique seu e-mail para confirmar.')
                except Exception as e:
                    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                        return JsonResponse({'status': 'warning', 'message': 'Sua inscrição foi registrada, mas houve um problema ao enviar o e-mail de confirmação.'})
                    else:
                        messages.warning(request, 'Sua inscrição foi registrada, mas houve um problema ao enviar o e-mail de confirmação.')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'Erro no formulário. Por favor, verifique os dados informados.'})
            else:
                messages.error(request, 'Erro no formulário. Por favor, verifique os dados informados.')
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'})
    else:
        return redirect('core:home')

def newsletter_confirmar(request, token):
    """View para confirmar inscrição na newsletter"""
    # Aqui você implementaria a lógica para confirmar a inscrição
    # Como é apenas uma estrutura base, esta funcionalidade não está completa
    messages.success(request, 'Inscrição confirmada com sucesso! Obrigado por se inscrever em nossa newsletter.')
    return redirect('core:home')

def newsletter_cancelar(request, token):
    """View para cancelar inscrição na newsletter"""
    # Aqui você implementaria a lógica para cancelar a inscrição
    # Como é apenas uma estrutura base, esta funcionalidade não está completa
    messages.info(request, 'Sua inscrição foi cancelada.')
    return redirect('core:home')