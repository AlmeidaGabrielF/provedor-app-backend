from django.db import models

class Pagamentos(models.Model):
    boleto = models.ForeignKey('boletos.Boleto', on_delete=models.CASCADE)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"Pagamento {self.id}"
    
