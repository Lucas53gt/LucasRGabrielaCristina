from django.db import models

class imovel(models.Model):
    incluir_anuncio = models.CharField(max_length=100) 
    consultar_anuncio = models.CharField(max_length=100)
    alterar_anuncio = models.CharField(max_length=100) 
    remover_anuncio = models.CharField(max_length=100) 
    
    def strg (self):
        return self.imovel
