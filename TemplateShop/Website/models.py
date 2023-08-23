from django.db import models
from datetime import datetime

# Create your models here.
class Site(models.Model):
    nome_card = models.CharField(max_length=200)
    description = models.TextField()
    path = models.TextField()
    primeiro_texto = models.TextField()
    segundo_texto = models.TextField()
    usuario = models.IntegerField()
    date_create = models.DateTimeField(default=datetime.now, blank = True)