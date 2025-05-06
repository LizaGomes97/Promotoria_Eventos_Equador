# contato/models.py
from django.db import models

class Contato(models.Model):
    ASSUNTO_CHOICES = (
        ('informacao', 'Solicitar Informação'),
        ('orcamento', 'Solicitar Orçamento'),
        ('parceria', 'Proposta de Parceria'),
        ('outro', 'Outro Assunto'),
    )
    
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    assunto = models.CharField(max_length=20, choices=ASSUNTO_CHOICES)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)
    respondido = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.nome} - {self.get_assunto_display()}"
    
    class Meta:
        ordering = ['-data_envio']
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Assinante da Newsletter'
        verbose_name_plural = 'Assinantes da Newsletter'