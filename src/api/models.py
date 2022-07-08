import email
from mailbox import NotEmptyError
from django.db import models

# Create your models here.
class ModeloBase(models.Model):
    """Classe base da modelo, que as demais classes herdarão."""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Pessoa(ModeloBase):
    """Classe pessoa"""
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)

class Funcionario(ModeloBase):
    """Classe Funcionário."""
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    funcao = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    ano_nascimento = models.IntegerField()


class Perfil(ModeloBase):
    nome = models.CharField(max_length=30)
    sobrenome =models.CharField(max_length=30)
    email = models.EmailField()
    github = models.URLField()
    avatar = models.ImageField()
    celular = models.CharField(max_length=20)
    perfil = models.TextField()

class Curriculo(ModeloBase):
    empresa = models.CharField(max_length=120)
    data_inicio = models.DateTimeField()
    data_saída = models.DateTimeField()
    empresa_atual = models.BooleanField()
    resumo = models.TextField    
    

 


