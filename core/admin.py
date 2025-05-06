# core/admin.py
from django.contrib import admin
from .models import Configuracao, Banner, SobreNos, Equipe, Depoimento, Parceiro, FAQ

@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('nome_site', 'email_contato', 'telefone', 'horario_funcionamento')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome_site', 'logo', 'favicon', 'descricao_meta', 'palavras_chave')
        }),
        ('Contato', {
            'fields': ('email_contato', 'telefone', 'whatsapp', 'endereco', 'horario_funcionamento')
        }),
        ('Redes Sociais', {
            'fields': ('facebook', 'instagram', 'youtube', 'linkedin')
        }),
    )

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'ativo', 'ordem')
    list_filter = ('ativo',)
    list_editable = ('ativo', 'ordem')
    search_fields = ('titulo', 'subtitulo')

@admin.register(SobreNos)
class SobreNosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo')
    
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ordem')
    list_editable = ('ordem',)
    search_fields = ('nome', 'cargo')

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'empresa', 'data', 'destaque')
    list_filter = ('destaque', 'data')
    list_editable = ('destaque',)
    search_fields = ('cliente', 'empresa', 'texto')

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'website', 'ordem')
    list_editable = ('ordem',)
    search_fields = ('nome',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pergunta', 'ordem')
    list_editable = ('ordem',)
    search_fields = ('pergunta', 'resposta')