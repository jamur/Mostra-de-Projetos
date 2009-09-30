#-*- coding: utf-8 -*-
from cadproj.models import OrientadorOuMediador, Projeto, Curso, TipoDeProjeto, ModoDeApresentacao, Cidade, Recurso, Calouro, Turma
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
    list_display = ('estudante', 'titulo', 'orientador_ou_mediador')
    fieldsets = (
        (None, {
            'fields': ('estudante','matricula','titulo','descricao')
        }),
        ('Outros Componentes da Equipe', {
            'fields': ('estudante2','estudante3','outros_componentes')
        }),
        ('Curso', {
            'fields': ('curso','turma')
        }),
        ('Contato', {
            'fields': ('cidade_onde_mora','fone','email')
        }),
        ('Projeto', {
            'fields': ('orientador_ou_mediador','colaborador','tipo_de_projeto','outro_tipo_de_projeto','palavra_chave1','palavra_chave2','palavra_chave3','cidade_de_abrangencia','local_e_ou_instituicao_de_abrangencia')
        }),
        ('Apresentação', {'fields':('modo_de_apresentacao','outro_modo','recursos_para_a_apresentacao')
        }),
    )
    list_per_page = 25
    search_fields = ['estudante', 'titulo', 'descricao', 'matricula', 'fone']
    list_filter = ('orientador_ou_mediador','curso','tipo_de_projeto','cidade_de_abrangencia')

admin.site.register(Curso)
admin.site.register(Projeto,ProjetoOptions)
admin.site.register(TipoDeProjeto)
admin.site.register(ModoDeApresentacao)

admin.site.register(OrientadorOuMediador)

admin.site.register(Cidade)
admin.site.register(Recurso)
admin.site.register(Calouro)
admin.site.register(Turma)

