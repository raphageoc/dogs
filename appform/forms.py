# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from appform.models import Dogs

class Dogform(ModelForm):
    class Meta:
        model = Dogs
        fields = ('foto','nome','porte', 'raca','idade','ponto',)

class Apresentform(ModelForm):
    class Meta:
        model = Dogs
        fields = ('foto','nome','porte', 'raca','idade','ponto',)
