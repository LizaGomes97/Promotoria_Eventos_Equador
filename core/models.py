# core/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Configuracao(models.Model):
    nome_site = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='site/')
    favicon = models.ImageField(upload_to='site/')
    email_contato = models.EmailField()
    telefone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField()
    horario_funcionamento = models.CharField(max_length=200)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    descricao_meta = models.CharField(max_length=160, help_text="Descrição para SEO (máximo 160 caracteres)")
    palavras_chave = models.CharField(max_length=200, help_text="Palavras-chave separadas por vírgula")
    
    def __str__(self):
        return self.nome_site
    
    class Meta:
        verbose_name = 'Configuração do Site'
        verbose_name_plural = 'Configurações do Site'

class Banner(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)
    texto_botao = models.CharField(max_length=30, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class SobreNos(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    texto = RichTextField()
    imagem = models.ImageField(upload_to='sobre/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="URL do vídeo do YouTube")
    
    def save(self, *args, **kwargs):
        """Implementação do padrão Singleton: Nunca cria um novo registro se já existe um"""
        self.pk = 1  # Sempre salva com o ID 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        """Retorna a única instância, ou cria uma se não existir"""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Sobre Nós'
        verbose_name_plural = 'Sobre Nós'

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    bio = models.TextField()
    foto = models.ImageField(upload_to='equipe/')
    email = models.EmailField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Membro da Equipe'
        verbose_name_plural = 'Equipe'

class Depoimento(models.Model):
    cliente = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    texto = models.TextField()
    foto = models.ImageField(upload_to='depoimentos/', blank=True, null=True)
    data = models.DateField(auto_now_add=True)
    destaque = models.BooleanField(default=False)
    
    def __str__(self):
        return self.cliente
    
    class Meta:
        ordering = ['-data']
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

class Parceiro(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='parceiros/')
    website = models.URLField(blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'

class FAQ(models.Model):
    pergunta = models.CharField(max_length=200)
    resposta = RichTextField()
    ordem = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.pergunta
    
    class Meta:
        ordering = ['ordem']
        verbose_name = 'Pergunta Frequente'
        verbose_name_plural = 'Perguntas Frequentes'