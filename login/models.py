from django.db import models

class login(models.Model):
    email = models.CharField(max_length=100) 
    senha = models.CharField(max_length=100)
    permissão = models.CharField(max_length=100) 
    
    def strg (self):
        return self.login
