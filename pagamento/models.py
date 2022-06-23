from django.db import models

class pagamento(models.Model):
    valor_pag = models.CharField(max_length=100) 
    forma_pag = models.CharField(max_length=100)
    parcelas_pag = models.CharField(max_length=100) 
    data_pag = models.CharField(max_length=100) 
    banco_pag = models.CharField(max_length=100)
    agencia_pag = models.CharField(max_length=100)
    conta_pag = models.CharField(max_length=100)

    def strg (self):
        return self.pagamento
