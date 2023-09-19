from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Esfirras(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Pedidos(models.Model):
    nome_cliente = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome_cliente


class Quantidade(models.Model):
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, null=True)
    nome = models.ForeignKey(Esfirras, on_delete=models.SET_NULL, null=True)
    qtd = models.IntegerField(default=0)
