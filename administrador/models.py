from django.db import models

class administrador(models.Model):
   
    calcular_salario= models.CharField(max_length=100) 
    
    def strg (self):
        return self.calcular_salario