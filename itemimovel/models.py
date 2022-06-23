from django.db import models

class itemimovel(models.Model):
    fotos = models.CharField(max_length=100) 
    
    def strg (self):
        return self.itemimovel