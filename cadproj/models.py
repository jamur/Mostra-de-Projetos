# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length = 75)

class Estudante(Pessoa):
    matricula = models.CharField('Código da Matrícula', max_length = 15)

    def __unicode__(self):
        return self.nome
    
class Orientador(Pessoa):

    def __unicode__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.nome

class TipoDeProjeto(models.Model):
    tipo = models.CharField(max_length = 35)

    def __unicode__(self):
        return self.tipo

class PalavraChave(models.Model):
    palavra = models.CharField(max_length = 65)

    def __unicode__(self):
        return self.palavra

class ModoDeApresentacao(models.Model):
    modo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.modo

class Cidade(models.Model):
    cidade = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.cidade

class Local(models.Model):
    local = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.local

class Recurso(models.Model):
    recurso = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.recurso

class Projeto(models.Model):
    titulo = models.CharField('Título do Projeto', max_length = 150) 
    descricao = models.TextField('Descrição do Projeto')
    estudante = models.ForeignKey(Estudante, related_name='projetos')
    orientador = models.ForeignKey(Orientador)
    coparticipante = models.ManyToManyField(Estudante, null=True, blank=True) #, related_name='projs')
    curso = models.ForeignKey(Curso, null=True, blank=True)
    tipo_de_projeto = models.ForeignKey(TipoDeProjeto, null=True, blank=True)
    tipo_exotico = models.CharField(max_length = 50, null=True, blank=True)
    palavra_chave = models.ManyToManyField(PalavraChave)
    modo_de_apresentacao = models.ForeignKey(ModoDeApresentacao, null=True, blank=True)
    outro_modo = models.TextField(null=True, blank=True)
    cidade_de_abrangencia = models.ManyToManyField(Cidade, null=True, blank=True)
    local_de_abrangencia = models.ManyToManyField(Local, null=True, blank=True)
    materiais_para_a_apresentacao = models.TextField(null=True, blank=True)
    recurso_para_a_apresentacao = models.ManyToManyField(Recurso, null=True, blank=True)

    def __unicode__(self):
        return self.titulo

