# -*- coding: utf-8 -*-
from django.db import models

ANO_DE_ENTRADA = (
    ('2005','2005'),
    ('2006','2006'),
    ('2007','2007'),
    ('2008','2008'),
    ('2009','2009'),
)

class Turma(models.Model):
    ano = models.CharField(max_length = 4)

    def __unicode__(self):
        return self.ano

# Create your models here.
class OrientadorOuMediador(models.Model):
    nome = models.CharField(max_length = 75)
    fone = models.CharField(max_length = 25, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    cidade = models.CharField(max_length = 50, blank = True, null = True)

    def __unicode__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.nome

class Calouro(models.Model):
    nome = models.CharField(max_length = 75)
    matricula = models.CharField(max_length = 25)
    fone = models.CharField(max_length = 25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    cidade = models.CharField(max_length = 50)
    curso = models.ForeignKey(Curso)
    turma = models.ForeignKey(Turma)

    def __unicode__(self):
        return self.nome

class TipoDeProjeto(models.Model):
    tipo = models.CharField(max_length = 35)

    def __unicode__(self):
        return self.tipo

class ModoDeApresentacao(models.Model):
    modo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.modo

class Cidade(models.Model):
    cidade = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.cidade

class Recurso(models.Model):
    recurso = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.recurso

class Projeto(models.Model):
    estudante = models.CharField('Estudante', max_length= 90, help_text = 'Nome "Completo" do Estudante ou Egresso idealizador do Projeto')
    matricula = models.CharField( null= True, blank= True, max_length = 25)
    titulo = models.TextField('Título ou Tema do Projeto', max_length = 150) 
    descricao = models.TextField('Breve Descrição do Projeto')
    estudante2 = models.CharField(max_length = 90,null=True,blank=True)
    estudante3 = models.CharField(max_length = 90,null=True,blank=True)
    outros_componentes = models.CharField('Outros componentes',max_length = 150, null=True, blank=True) #, related_name='projs')
    cidade_onde_mora = models.CharField(max_length = 50)
    fone = models.CharField("Fone(s)", max_length = 25, null=True, blank=True)
    email = models.EmailField("Email", null=True,blank=True)
    orientador_ou_mediador = models.ForeignKey(OrientadorOuMediador)
    colaborador = models.CharField(max_length = 100, null=True, blank=True, help_text="Preencha caso haja um colaborador do projeto (técnico, professor ou outro)")
    curso = models.ForeignKey(Curso)
    turma = models.ForeignKey(Turma)
    tipo_de_projeto = models.ForeignKey(TipoDeProjeto)
    outro_tipo_de_projeto = models.CharField('Outro',max_length = 50, null=True, blank=True)
    palavra_chave1 = models.CharField(max_length=50)
    palavra_chave2 = models.CharField(max_length=50)
    palavra_chave3 = models.CharField(max_length=50)
    modo_de_apresentacao = models.ForeignKey(ModoDeApresentacao)
    outro_modo = models.CharField(max_length=50, null=True, blank=True)
    cidade_de_abrangencia = models.ManyToManyField(Cidade)
    local_e_ou_instituicao_de_abrangencia = models.CharField(max_length=150, verbose_name="Local e/ou Instituição de Abrangência")
    recursos_para_a_apresentacao = models.ManyToManyField(Recurso)

    def __unicode__(self):
        return self.titulo

