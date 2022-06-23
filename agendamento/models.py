from django.db import models

class agendamento(models.Model): 
    incluir_agendamento= models.CharField(max_length=100) 
    consultar_agendamento = models.CharField(max_length=100)
    alterar_agendamento = models.CharField(max_length=100) 
    remover_agendamento = models.CharField(max_length=100) 
    def strg (self):
        return self.agendamento
