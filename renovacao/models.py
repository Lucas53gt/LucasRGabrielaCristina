from django.db import models

# Create your models here.
class renovacao(models.Model):
    dataDesoculpacao = models.CharField(max_length=100) 
    dataRenovacao = models.CharField(max_length=100)
    cartorio = models.CharField(max_length=100) 
    
    def strg (self):
        return self.renovacao