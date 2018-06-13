# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models  ########################## importa a biblioteca models do modulo gis que contém o tipos de dados normais e espaciais
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Dogs(models.Model):
    id = models.AutoField(primary_key=True) ########################## cria um campo do tipo serial e definido com chave primaria da classe
    nome = models.CharField(max_length=50) ########################## cria um campo do tipo texto com tamanho máximo de 50 caracteres (char)
    raca = models.CharField(max_length=50)
    porte = models.CharField(max_length=50)
    idade = models.CharField(max_length=50)
    foto = models.ImageField()             ########################## cria um campo do tipo imagem
    ponto = models.PointField(srid=4326)   ########################## cria um campo do tipo ponto com o sistema de referencia definido com wgs84

    def __str__(self):
        return self.nome
