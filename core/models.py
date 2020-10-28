from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Sexo(models.Model):
    descricao = models.CharField(max_length=30)
    def __str__(self):
        return self.descricao
    

class EstadoCivil(models.Model):
    descricao = models.CharField(max_length=30)
    def __str__(self):
        return self.descricao

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30, verbose_name='Sobrenome')
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, blank=True,null=True)
    endereco = models.CharField(max_length=30, verbose_name='Endereço')
    identidade = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    cep = models.CharField(max_length=30)
    datanascimento = models.DateTimeField(blank=True,null=True, verbose_name='Data de nascimento')
    estadoCivil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, blank=True,null=True, verbose_name='Estado civil')

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ("nome", "ultimo_nome")
    
    def __str__(self):
        return f"{self.nome} {self.ultimo_nome}"

class Produto(models.Model):
    descricao = models.CharField(max_length=30, verbose_name='Descrição')
    preco = models.IntegerField(verbose_name='Preço')
    class Meta:
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return f"{self.descricao}"

class ProdutoComprado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.IntegerField(verbose_name='Preço')
    class Meta:
        verbose_name_plural = "Produtos comprados"
    
    def __str__(self):
        return f"{self.produto}"
    