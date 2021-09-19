from django.contrib import admin
from.models import Empresa, Usuario, Jogo

class Listar_Empresa(admin.ModelAdmin):
    list_display = ('id', 'nome', 'pais')
    list_display_links = ('id', 'nome')
    search_fields = ('nome' ,)
    list_filter = ('pais' ,)
    list_per_page = 5


class Listar_Usuario(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

class Listar_Jogo(admin.ModelAdmin):
    list_display = ('id', 'nome', 'generos', 'publicado')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_filter = ('generos', )
    list_editable = ('publicado', )
    list_per_page = 5

admin.site.register(Empresa, Listar_Empresa)
admin.site.register(Usuario, Listar_Usuario)
admin.site.register(Jogo, Listar_Jogo)


# Register your models here.
