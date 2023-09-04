from django.db import models
from datetime import datetime

# Create your models here.
class RoupaPromo(models.Model):
    nome_produto = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    path = models.ImageField( upload_to="images/")
    preco_produto = models.DecimalField(default=000.00, max_digits=5, decimal_places=2)
    desconto = models.IntegerField(default=0)
    usuario = models.CharField(max_length=20)
    date_create = models.DateTimeField(default=datetime.now, blank = True)

class RoupaSocial(models.Model):
    nome_produto = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    path = models.ImageField( upload_to="images/")
    preco_produto = models.DecimalField(default=000.00, max_digits=5, decimal_places=2)
    usuario = models.CharField(max_length=20)
    date_create = models.DateTimeField(default=datetime.now, blank = True)

class RoupaCasual(models.Model):
    nome_produto = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    path = models.ImageField(upload_to="images/")
    preco_produto = models.DecimalField(default= 000.00, max_digits=5, decimal_places=2)
    usuario = models.CharField(max_length=20)
    date_create = models.DateTimeField(default=datetime.now, blank= True)

class Usuario(models.Model):
     email = models.EmailField()
     senha = models.TextField(max_length=255)
     lembrar = models.BooleanField(default= False)

class Carrossel(models.Model):
    carrossel = models.ImageField(upload_to="images/")
    description = models.TextField(max_length=255)
    buttom = models.CharField(default='', max_length=30)
    title = models.CharField(default='', max_length=30)

class Icons(models.Model):
    icones = models.ImageField(upload_to="images/")

class Imagens(models.Model):
    imagens = models.ImageField(upload_to="images/")

class Depoimentos(models.Model):
    usuario = models.CharField(max_length=200)
    depoimento = models.TextField(max_length=255)
    date_create = models.DateField(default= datetime.now, blank= True)