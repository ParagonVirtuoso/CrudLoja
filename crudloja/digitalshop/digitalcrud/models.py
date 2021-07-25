from django.db import models

class Calcados(models.Model):
    nome = models.CharField(max_length=50)
    materialinterno = models.CharField(max_length=15)
    materialsola = models.CharField(max_length=15)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    cor = models.CharField(max_length=20)
    ocasiao = models.CharField(max_length=50)
    tamanho = models.IntegerField()
    objects = models.Manager()
