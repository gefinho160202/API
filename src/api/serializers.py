from pyexpat import model
from .models import Pessoa, Funcionario
from rest_framework import serializers


class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id','nome','sobrenome','created_at','updated_at']

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id','nome','sobrenome','created_at','updated_at',
        'funcao','email','ano_nascimento']        