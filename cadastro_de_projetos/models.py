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

class Projeto(models.Model):
    titulo = models.CharField('Título do Projeto', max_length = 150) 
    descricao = models.TextField('Descrição do Projeto')
    estudante = models.ForeignKey(Estudante)
    orientador = models.ForignKey(Orientador)

    def __unicode__(self):
        return self.titulo
