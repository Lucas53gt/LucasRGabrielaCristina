from django.db import models


class locacao(models.Model):
    dataDeOcupação = models.CharField(max_length=100) 
    periodo = models.CharField(max_length=100)
    forma_garantia = models.CharField(max_length=100) 
    fiador = models.CharField(max_length=100) 
    
    def strg (self):
        return self.locacao
