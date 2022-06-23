from django.db import models

# Create your models here.
class pessoa(models.Model):
    matricula = models.CharField(max_length=100) 
    telefone = models.CharField(max_length=100)
    cep = models.CharField(max_length=100) 
    rua = models.CharField(max_length=100) 
    bairro = models.CharField(max_length=100)
    cidade= models.CharField(max_length=100) 
    uf = models.CharField(max_length=100) 
    
    
    def strg (self):
        return self.pessoa