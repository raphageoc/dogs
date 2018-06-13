# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render          ######################### importa a função para renderizar as paginas html
from django.http import HttpResponseRedirect
from .forms import Dogform                   ########################## importa o formulario  Dogform definido no arquivo forms
from appform.models import Dogs               ######################### importa o modelo de dados Dogs  definido no arquivo models
from django.contrib.gis.geos import GEOSGeometry  ######################### importa a funçao geosgeometry que codifica diversos formatos em tipo geometry (postgis)
import json                                       ######################### importa a biblioteca para manipular arquivos do formato json
# Create your views here.

def apresenta(request):
    img = Dogs.objects.all() #########################  requisita todos as linhas da tabela dogs do banco de dados
    return render(request, 'appform/apresenta.html',{'img': img} ) ######################### retorna a pagina apresenta.html e passa como parametros todas as linhas da tabela dogs do banco de dados


def site(request):

    form = Dogform ######################### cria uma nova instancia do formulario dogform
    return render(request, 'appform/main.html',{'form': form} ) ######################### retorna a pagina main.html e passa como parametro o formulario dogform


def add_dog(request):

    if request.method == 'POST': ######################## verifica se a requisição utiliza o método http POST
        form = Dogform(request.POST, request.FILES) ######################## cria uma instancia do formulário dogform com as informações passadas pelo no request que veio das paginas html,
        p = request.POST['geojson'] ######################## pega a coordenada em geojson que é inserida na pagina web no input do "Form html"
        data = json.loads(p) ######################## decodifica o geojson e transforma em um dicionário
        p=data['geometry'] ######################## pega a parte de geometria do geojson necessario para codificar utilizando a biblioteca GEOS
        p = json.dumps(p) ######################## codifica p como geojson
        form.ponto = GEOSGeometry(p) ########################codifica o geojson como geometry para inserir no banco


        updated_data = request.POST.copy() ######################## faço uma cópia das informações passadas no request
        updated_data.update({'ponto': p})  ######################## modifico a cópia do request trocando formato  do ponto de geojson para geometry
        form = Dogform(updated_data, request.FILES) ######################## instancio o formulario com as informações modificadas e com os arquivos upados

        if form.is_valid():  ######################## verifico se o formulario instaciado é valido
            form.save() ######################## salvo o formulario no banco

        else:
            print form.errors ######################## se ocorrer algum erro é printado



    return render(request, 'appform/main.html', {'form': form}) ######################## apos adicionado o objeto é retonado a mesma pagina com o formulario
