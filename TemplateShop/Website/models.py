from django.db import models
from datetime import datetime

# Create your models here.
class Site(models.Model):
    nome_produto = models.CharField(max_length=200)
    description = models.TextField()
    path = models.TextField()
    preco_produto = models.DecimalField(max_digits=5, decimal_places=2)
    imagem_produto = models.ImageField()
    usuario = models.CharField(max_length=20)
    date_create = models.DateTimeField(default=datetime.now, blank = True)