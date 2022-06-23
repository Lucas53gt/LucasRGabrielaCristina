from django.db import models

class boleto(models.Model):
    codCliente = models.CharField(max_length=100) 
    nomeCliente = models.CharField(max_length=100)
    
    
    def strg (self):
        return self.boleto
