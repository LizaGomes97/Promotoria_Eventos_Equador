# eventos/models.py
from django.db import models
from ckeditor.fields import RichTextField

class TipoEvento(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(blank=True, null=True)
    icone = models.ImageField(upload_to='tipos_eventos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Tipo de Evento'
        verbose_name_plural = 'Tipos de Eventos'

class Evento(models.Model):
    STATUS_CHOICES = (
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    )
    
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    tipo = models.ForeignKey(TipoEvento, on_delete=models.CASCADE, related_name='eventos')
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    endereco = models.TextField()
    descricao_curta = models.TextField(max_length=300)
    descricao = RichTextField()
    imagem_principal = models.ImageField(upload_to='eventos/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendado')
    destaque = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-data_inicio']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

class ImagemEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='eventos/')
    titulo = models.CharField(max_length=100, blank=True, null=True)
    destaque = models.BooleanField(default=False)
    ordem = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Imagem de {self.evento.nome}"
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Imagem do Evento'
        verbose_name_plural = 'Imagens dos Eventos'

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descricao_curta = models.TextField(max_length=300)
    descricao = RichTextField()
    icone = models.CharField(max_length=50, help_text="Nome do ícone Font Awesome (ex: fa-calendar)")
    imagem = models.ImageField(upload_to='servicos/')
    destaque = models.BooleanField(default=False)
    ordem = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Portfolio(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    cliente = models.CharField(max_length=100)
    data = models.DateField()
    descricao = RichTextField()
    imagem_principal = models.ImageField(upload_to='portfolio/')
    destaque = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-data']
        verbose_name = 'Projeto do Portfólio'
        verbose_name_plural = 'Projetos do Portfólio'

class ImagemPortfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='portfolio/')
    titulo = models.CharField(max_length=100, blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Imagem de {self.portfolio.titulo}"
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Imagem do Portfólio'
        verbose_name_plural = 'Imagens do Portfólio'