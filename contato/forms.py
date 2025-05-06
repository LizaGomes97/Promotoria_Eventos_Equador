# contato/forms.py
from django import forms
from .models import Contato, Newsletter

class ContatoForm(forms.ModelForm):
    """Formulário para contato"""
    
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu telefone'}),
            'assunto': forms.Select(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua mensagem', 'rows': 5}),
        }

class NewsletterForm(forms.ModelForm):
    """Formulário para inscrição na newsletter"""
    
    class Meta:
        model = Newsletter
        fields = ['email', 'nome']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome (opcional)'}),
        }