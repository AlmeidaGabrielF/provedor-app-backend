from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    velocidade = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
            return self.nome