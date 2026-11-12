from django.db import models

class Menu(models.Model):
    titulo = models.CharField(max_lenght=100),
    destino = models.CharField(max_lenght=100),
    ordem = models.IntegerField(default=0),
    ativo = models.BooleanField(default=False),
