# -*- coding: utf-8 -*-
from django.db import models

ANO_DE_ENTRADA = (
    ('2005','2005'),
    ('2006','2006'),
    ('2007','2007'),
    ('2008','2008'),
    ('2009','2009'),
)

class AnoDeEntrada(models.Model):
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
    fone = models.CharField(max_length = 25)
    email = models.EmailField()
    cidade = models.CharField(max_length = 50)
    curso = models.ForeignKey(Curso)
    ano_de_entrada = models.ForeignKey(AnoDeEntrada)

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
    titulo = models.TextField('Título ou Tema do Projeto', max_length = 150) 
    descricao = models.TextField('Breve Descrição do Projeto')
    estudante = models.CharField('Estudante ou Egresso', max_length= 90)
    estudante2 = models.CharField(max_length = 90,null=True,blank=True)
    estudante3 = models.CharField(max_length = 90,null=True,blank=True)
    outros_componentes = models.CharField('Outros componentes',max_length = 150, null=True, blank=True) #, related_name='projs')
    cidade_onde_mora = models.CharField(max_length = 50)
    fone = models.CharField(max_length = 25, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    orientador_ou_mediador = models.ForeignKey(OrientadorOuMediador)
    curso = models.ForeignKey(Curso)
    ano_de_entrada = models.ForeignKey(AnoDeEntrada)
    tipo_de_projeto = models.ForeignKey(TipoDeProjeto, null=True, blank=True)
    outro_tipo_de_projeto = models.CharField('Outro',max_length = 50, null=True, blank=True)
    palavra_chave1 = models.CharField(max_length=50)
    palavra_chave2 = models.CharField(max_length=50)
    palavra_chave3 = models.CharField(max_length=50)
    modo_de_apresentacao = models.ForeignKey(ModoDeApresentacao, null=True, blank=True)
    outro_modo = models.CharField(max_length=50, null=True, blank=True)
    cidade_de_abrangencia = models.ManyToManyField(Cidade, null=True, blank=True)
    local_de_abrangencia = models.CharField(max_length=150, null=True, blank=True)
    recursos_para_a_apresentacao = models.ManyToManyField(Recurso, null=True, blank=True)

    def __unicode__(self):
        return self.titulo

