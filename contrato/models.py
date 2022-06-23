from django.db import models

class contrato(models.Model):
    dadosCliente = models.CharField(max_length=100) 
    dadosCorretor = models.CharField(max_length=100)
    descriçãoImovel = models.CharField(max_length=100)
    valor = models.CharField(max_length=100) 
    documentação = models.CharField(max_length=100)
    clausulaPenal = models.CharField(max_length=100)
    
    def strg (self):
        return self.contrato
