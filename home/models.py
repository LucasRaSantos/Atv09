from django.db import models

class Conteudo(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    slug = models.SlugField(unique=True, verbose_name="Slug (URL amigável)")
    conteudo_html = models.TextField(
        verbose_name="Conteúdo HTML",
        help_text="Insira apenas o HTML interno (<section>, <article>, <p>, etc.), sem <html>, <head>, <body>, <header>, <nav> ou <footer>."
    )
    ativo = models.BooleanField(default=False, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Conteúdo"
        verbose_name_plural = "Conteúdos"
        
    def __str__(self):
        return self.titulo
    
class Menu(models.Model):
    TIPO_CHOICES = [
        ('interno', 'Conteúdo interno'),
        ('externo', 'Link externo'),
    ]

    titulo = models.CharField(max_length=100, verbose_name="Título do Menu")
    tipo_destino = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='interno',
        verbose_name="Tipo de destino"
    )
    ordem = models.PositiveIntegerField(default=0, verbose_name="Ordem de exibição")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    # Relacionamento usado quando o destino for interno
    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Conteúdo interno relacionado"
    )
    
    # URL usada quando o destino for externo
    url_externa = models.URLField(
        blank=True,
        null=True,
        verbose_name="URL externa"
    )

    class Meta:
        ordering = ['ordem']
        verbose_name = "Item de Menu"
        verbose_name_plural = "Itens de Menu"

    def __str__(self):
        return f"{self.ordem} - {self.titulo}"
