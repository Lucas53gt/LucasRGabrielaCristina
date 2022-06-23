from django.db import models

# Create your models here.
class Pessoa_Juridica(models.Model):
    cnpj = models.CharField(max_length=100) 
    razaoSocial = models.CharField(max_length=100)
    representanteLegal = models.CharField(max_length=100) 
    
    def strg (self):
        return self.Pessoa_Juridica