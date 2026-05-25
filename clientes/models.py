from django.db import models

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=200, verbose_name="Nome Completo")
    CPF = models.CharField(unique=True, max_length=14, verbose_name="CPF")
    nascimento = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(unique=True, max_length=100, verbose_name="E-mail")
    endereco = models.CharField(max_length=100, verbose_name="Endereço Completo")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    pagamento = models.DateField(verbose_name="Data de Pagamento")
    
    def __str__(self):
        return self.nome_completo
    
    plano = models.ForeignKey('planos.Plano', on_delete=models.CASCADE)