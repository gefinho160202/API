

# Create your views here.
from dataclasses import dataclass
import email
import json
from pickle import FALSE
import re
from django.http import JsonResponse
from .models import Pessoa,Funcionario
from .serializers import FuncionarioSerializer, PessoaSerializer

def health(request):
    return JsonResponse({"mensagem": "ok"}, safe=False)


def funcionario_info(request):
    """View de funcionário."""
    query_params = request.GET
    if request.method == 'GET':
        qs_funcionario = Funcionario.objects.all().values()
        serializer = FuncionarioSerializer(qs_funcionario, many=True)
        return JsonResponse({"funcionarios": serializer.data})

    if request.method == 'POST':
        data = json.loads(request.body)

        funcionario = Funcionario()
        funcionario.ano_nascimento = data.get('ano_nascimento')
        funcionario.nome = data.get('nome')
        funcionario.sobrenome = data.get('sobrenome')
        funcionario.email = data.get('email')
        funcionario.funcao = data.get('funcao')

        existe_funcionario = Funcionario.objects.filter(email=funcionario.email).count()
        if existe_funcionario:
            return JsonResponse({"mensagem": "O usuário já existe"})
        
        funcionario.save()
        serializer = FuncionarioSerializer(funcionario, many=False)
        return JsonResponse(serializer.data)

    if request.method == 'DELETE':
        existe_email = query_params.get('email')

        if existe_email:
            existe_funcionario = Funcionario.objects.filter(email=existe_email).first()

            if existe_email:
                serializer = FuncionarioSerializer(existe_funcionario, many=False)
                existe_funcionario.delete()
                return JsonResponse({"objeto": serializer.data})

        return JsonResponse({"mensagem": 'Usuário não encontrado'})   

    if request.method == 'PUT':
        data = json.loads(request.body)
        email = query_params.get('email')

        email_existe = Funcionario.objects.filter(email=data.get('email')).count()

        funcionario = Funcionario.objects.filter(email=email).first()
        if funcionario:
            funcionario.ano_nascimento = data.get('ano_nascimento')
            funcionario.sobrenome = data.get('nome')
            funcionario.email = data.get('email')
            funcionario.funcao = data.get('funcao')
            funcionario.save()
            serializer = FuncionarioSerializer(funcionario, many=False)
            return JsonResponse(serializer.data)

        return JsonResponse({'mensagem': 'Usuário não encontrado'})    
            

    return JsonResponse({'mensagem': 'método update'})         


    return JsonResponse({"mensagem": "Método inválido"})
















