from django.db import models

class aviso(models.Model):
    incluir_aviso = models.CharField(max_length=100) 
    consultar_aviso = models.CharField(max_length=100)
    remover_aviso = models.CharField(max_length=100) 
    
    def strg (self):
        return self.aviso
