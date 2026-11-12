from django.db import models

class Conteudo(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    conteudo = models.TextField(null=True)
    ativo = models.BooleanField(default=False)
    
