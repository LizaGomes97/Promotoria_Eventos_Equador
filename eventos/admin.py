# eventos/admin.py
from django.contrib import admin
from .models import TipoEvento, Evento, ImagemEvento, Servico, Portfolio, ImagemPortfolio

class ImagemEventoInline(admin.TabularInline):
    model = ImagemEvento
    extra = 1

@admin.register(TipoEvento)
class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ('nome',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'data_inicio', 'data_fim', 'local', 'cidade', 'status', 'destaque')
    list_filter = ('tipo', 'status', 'destaque', 'data_inicio')
    list_editable = ('status', 'destaque')
    search_fields = ('nome', 'descricao_curta', 'local', 'cidade')
    prepopulated_fields = {'slug': ('nome',)}
    date_hierarchy = 'data_inicio'
    inlines = [ImagemEventoInline]
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'slug', 'tipo', 'descricao_curta', 'descricao', 'imagem_principal', 'status', 'destaque')
        }),
        ('Data e Local', {
            'fields': ('data_inicio', 'data_fim', 'local', 'cidade', 'endereco')
        }),
    )

class ImagemPortfolioInline(admin.TabularInline):
    model = ImagemPortfolio
    extra = 1

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao_curta', 'destaque', 'ordem')
    list_filter = ('destaque',)
    list_editable = ('destaque', 'ordem')
    search_fields = ('nome', 'descricao_curta')
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'data', 'destaque')
    list_filter = ('destaque', 'data')
    list_editable = ('destaque',)
    search_fields = ('titulo', 'cliente', 'descricao')
    prepopulated_fields = {'slug': ('titulo',)}
    inlines = [ImagemPortfolioInline]