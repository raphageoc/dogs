# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^add_dog$', views.site, name='site'),  ########################## direciona as urls  para a view responsavel pela requisicao (Exemplo www.site.com/add_dog )
    url(r'consulta', views.add_dog),
    url(r'apresenta', views.apresenta),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) ########################## quando usar servidor de desenvolvimento deve-se indicar o local dos arquivos estaticos aqui

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ########################## quando usar servidor de desenvolvimento deve-se indicar o local dos uploads aqui
