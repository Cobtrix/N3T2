from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField()
    sinopse = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo