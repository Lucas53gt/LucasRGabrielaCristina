from django.db import models

class cliente(models.Model):
    consultar_imoveis = models.CharField(max_length=100) 
    manter_conta = models.CharField(max_length=100)
    agendar_visita = models.CharField(max_length=100) 
    
    def strg (self):
        return self.cliente