from django.contrib import admin
from .models import Conteudo, Menu

@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'conteudo_html')
    prepopulated_fields = {'slug': ('titulo',)} # Preenche o slug automaticamente ao digitar o título

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_destino', 'conteudo', 'url_externa', 'ordem', 'ativo')
    list_editable = ('ordem', 'ativo')
    list_filter = ('tipo_destino', 'ativo')
