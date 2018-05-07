# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Dogs(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    porte = models.CharField(max_length=50)
    idade = models.CharField(max_length=50)
    foto = models.ImageField()
    ponto = models.PointField(srid=4326)

    def __str__(self):
        return self.nome
