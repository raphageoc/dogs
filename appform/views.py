# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Dogform
from appform.models import Dogs
from django.contrib.gis.geos import GEOSGeometry
import json
# Create your views here.

def apresenta(request):
    img = Dogs.objects.all()
    return render(request, 'appform/apresenta.html',{'img': img} )


def site(request):

    form = Dogform
    return render(request, 'appform/main.html',{'form': form} )

# def dogs(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})







def add_dog(request):

    if request.method == 'POST':
        form = Dogform(request.POST, request.FILES)
        p = request.POST['geojson']
        data = json.loads(p)
        p=data['geometry']
        p = json.dumps(p)
        form.ponto = GEOSGeometry(p)


        updated_data = request.POST.copy()
        updated_data.update({'ponto': p})
        form = Dogform(updated_data, request.FILES)

        print(updated_data)

        if form.is_valid():
            form.save()

        else:
            print form.errors



    return render(request, 'appform/main.html', {})
