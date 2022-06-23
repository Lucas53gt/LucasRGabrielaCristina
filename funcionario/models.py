from django.db import models

class funcionario(models.Model):
    consultar_imovel = models.CharField(max_length=100) 
    manter_anuncio = models.CharField(max_length=100)
    manter_cliente = models.CharField(max_length=100) 
    manter_funcionario = models.CharField(max_length=100) 
    manter_agendamento = models.CharField(max_length=100)
    gerar_relatorio = models.CharField(max_length=100) 
    calcular_salario = models.CharField(max_length=100) 
    
    def strg (self):
        return self.funcionario
