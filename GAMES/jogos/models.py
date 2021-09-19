from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome= models.CharField(max_length=150)
    cidade= models.CharField(max_length=50)
    estado= models.CharField(max_length=50)
    pais= models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome= models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome= models.CharField(max_length=50)
    criador= models.CharField(max_length=50)
    datadelancamento= models.IntegerField()
    generos= models.CharField(max_length=50)
    plataformas= models.CharField(max_length=50)
    enredo= models.TextField()
    critica= models.CharField(max_length=150)
    avaliacao= models.CharField(max_length=50)
    desenvolvedores= models.ManyToManyField(Empresa)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    publicado= models.BooleanField(default=False)
    capa= models.ImageField(upload_to='capas/%d/%m/%y', blank=True)

    def __str__(self):
        return self.nome

