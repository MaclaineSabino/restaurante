from django.contrib.auth.models import User, Group
from django.db import models
import datetime
import decimal


# Create your models here.

class Mesa(models.Model):
    
    nome = models.CharField(max_length=50)
    status=models.CharField(max_length=10,default="livre")


    def Conta(self):
        conta,res = Conta.objects.get_or_create(mesa=self,status='aberta')
        
        return conta


class Conta(models.Model):
    mesa=models.ForeignKey(Mesa,
                                on_delete=models.CASCADE)
    data = models.DateField(default=datetime.date.today())
    valor_total=models.DecimalField(max_digits=9,decimal_places=2,default=0.00)
    status=models.CharField(max_length=10,default="aberta")

    def ocuparMesa(self):
        if self.mesa.status=='livre':
            self.mesa.status='ocupada'
            self.mesa.save()

    def desocuparMesa(self):
        if self.mesa.status=='ocupada':
            self.mesa.status='livre'
            self.mesa.save()

    def finalizarConta(self):
        self.status='encerrada'
        self.save()
        self.desocuparMesa()
        return self.valor_total


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome






class Produto(models.Model):

    nome = models.CharField(max_length=50)
    categoria=models.ForeignKey(Categoria,
                                on_delete=models.CASCADE,
                                )


class TipoProduto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=9,decimal_places=2)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE,
                                )

    def __str__(self):
        return self.nome






class ItemConta(models.Model):
    conta=models.ForeignKey(Conta,
                                on_delete=models.CASCADE,
                                related_name="contas")
    tipo_produto = models.ForeignKey(TipoProduto,
                                on_delete=models.CASCADE,
                                related_name="tipos_produtos")
    quantidade = models.IntegerField(default=0)

    parcial = models.DecimalField(max_digits=9,decimal_places=2,default=0.0)

    def despesaConta(self):
        montanteproduto = self.tipo_produto.valor

        self.conta.valor_total = decimal.Decimal(self.conta.valor_total)+montanteproduto
        self.conta.save()






