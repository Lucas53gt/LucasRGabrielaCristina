from django.db import models

class gerente(models.Model):
    calcular_salario = models.CharField(max_length=100) 
    
    def strg (self):
        return self.gerente
