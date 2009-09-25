#-*- coding: utf-8 -*-
from cadproj.models import Pessoa, Estudante, Orientador, Projeto, Curso, TipoDeProjeto, PalavraChave, ModoDeApresentacao, Local, Cidade, Recurso
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class PessoaOptions(admin.ModelAdmin):
    list_display = ('nome',)
    #list_filter = ('tipo_de_documento','local_atual','data_de_envio_ou_chegada','preenchido','assinado','estagiario')
    #search_fieldsets = ['nome']       # nao funcionou com foreign

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
admin.site.register(TipoDeProjeto)
admin.site.register(PalavraChave)
admin.site.register(ModoDeApresentacao)

admin.site.register(Pessoa, PessoaOptions)
admin.site.register(Estudante, EstudanteOptions)
admin.site.register(Orientador, OrientadorOptions)

admin.site.register(Projeto, ProjetoOptions)
admin.site.register(Cidade)
admin.site.register(Local)
admin.site.register(Recurso)

