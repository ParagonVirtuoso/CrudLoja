from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^calcado_list/', calcado_lista, name='listar_calcados'),
    url(r'^calcado_form/', calcado_novo, name='novo_calcado'),
    url(r'^calcado_edit/(?P<pk>[0-9]+)', calcado_editar, name='editar_calcado'),
url(r'^calcado_remove/(?P<pk>[0-9]+)', calcado_remove, name='remover_calcado'),
]
