from django.db import models

class Boleto(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.valor)
