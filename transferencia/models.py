from django.db import models

# Create your models here.
class transferencia(models.Model):
    tipo = models.CharField(max_length=100) 
    codIdentificacao = models.CharField(max_length=100)
    
    
    def strg (self):
        return self.transferencia