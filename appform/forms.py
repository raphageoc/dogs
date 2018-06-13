# -*- coding: utf-8 -*-
from django.db import models ######################## importa a classe model do django
from django.forms import ModelForm ######################## importa a classe modelform do django (para criar formularios direto dos modelos de dados)
from appform.models import Dogs ######################## importa a classe Dogs do modelo de dados

######################## cria o formulário para inserir dados dos cachorros 
class Dogform(ModelForm):
    class Meta:
        model = Dogs ######################## instancia a classe Dogs
        fields = ('foto','nome','porte', 'raca','idade','ponto',) ######################## define quais campos do nosso modelo de dados vai compor o formulario

class Apresentform(ModelForm):
    class Meta:
        model = Dogs
        fields = ('foto','nome','porte', 'raca','idade','ponto',)
