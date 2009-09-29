#-*- coding: utf-8 -*-
from cadproj.models import OrientadorOuMediador, Projeto, Curso, TipoDeProjeto, ModoDeApresentacao, Cidade, Recurso, Calouro, AnoDeEntrada
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class EstudanteOptions(admin.ModelAdmin):
    list_display = ('nome','matricula')
    #date_hierarchy = 'data_e_hora'
    
class OrientadorOptions(admin.ModelAdmin):
    list_display = ('nome',)

#class CursoOptions(admin.ModelAdmin):
    #list_display = ('nome',)

class ProjetoOptions(admin.ModelAdmin):
    #inlines = [Pendencia_Inline, Contatamento_Inline]
    list_display = ('titulo', 'estudante', 'orientador')
    fieldsets = (
        (None, {
            'fields': ('titulo','descricao','estudante','orientador','curso')
        }),
        ('Projeto', {
            'fields': ('tipo_de_projeto','tipo_exotico','palavra_chave')
        }),
        ('Abrangência', {'fields':('cidade_de_abrangencia','local_de_abrangencia')
        }),
        ('Apresentação', {'fields':('modo_de_apresentacao','materiais_para_a_apresentacao','recurso_para_a_apresentacao','outro_modo')
        }),
    )
    list_per_page = 25
    search_fields = ['titulo', 'descricao']
    list_filter = ('orientador','curso','tipo_de_projeto','cidade_de_abrangencia','local_de_abrangencia')

admin.site.register(Curso)
admin.site.register(Projeto)
admin.site.register(TipoDeProjeto)
admin.site.register(ModoDeApresentacao)

admin.site.register(OrientadorOuMediador)

admin.site.register(Cidade)
admin.site.register(Recurso)
admin.site.register(Calouro)
admin.site.register(AnoDeEntrada)

