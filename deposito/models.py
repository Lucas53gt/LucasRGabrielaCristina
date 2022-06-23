from django.db import models

class deposito(models.Model):
    idDeposito = models.CharField(max_length=100) 
    
    def strg (self):
        return self.deposito
