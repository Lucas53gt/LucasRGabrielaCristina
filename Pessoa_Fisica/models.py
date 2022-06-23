from django.db import models

# Create your models here.
class Pessoa_Fisica(models.Model):
    cpf = models.CharField(max_length=100) 
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100) 
    sexo = models.CharField(max_length=100)
    dataNascimento = models.CharField(max_length=100) 
    def strg (self):
        return self.cpf