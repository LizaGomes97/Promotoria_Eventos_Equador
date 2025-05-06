# contato/admin.py
from django.contrib import admin
from .models import Contato, Newsletter

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido', 'respondido')
    list_filter = ('assunto', 'lido', 'respondido', 'data_envio')
    list_editable = ('lido', 'respondido')
    search_fields = ('nome', 'email', 'mensagem')
    readonly_fields = ('data_envio',)
    fieldsets = (
        ('Informações do Contato', {
            'fields': ('nome', 'email', 'telefone', 'assunto', 'mensagem', 'data_envio')
        }),
        ('Status', {
            'fields': ('lido', 'respondido')
        }),
    )

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'nome', 'data_cadastro', 'ativo')
    list_filter = ('ativo', 'data_cadastro')
    list_editable = ('ativo',)
    search_fields = ('email', 'nome')
    readonly_fields = ('data_cadastro',)