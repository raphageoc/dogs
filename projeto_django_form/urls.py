# -*- coding: utf-8 -*-

"""projeto_django_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include     #### adiciona a funçao include e url para o projeto
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('appform.urls')),      ########## redireciona as requisições dos clientes para o arquivo url dentro da pasta do aplicativo
]
