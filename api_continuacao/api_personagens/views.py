from rest_framework.decorators import api_view
from .models import Obra, AtorDublador, Personagem, Habilidade, Relacionamento, PersonagemHabilidade
from .serializers import ObraSerializer, AtorDubladorSerializer, PersonagemSerializer, HabilidadeSerializer, RelacionamentoSerializer, PersonagemHabilidadeSerializer
from rest_framework.response import Response
from rest_framework import status
 
@api_view(['GET' 'DELETE'])
def obra_detalhe(request, id):
    try: 
        obra = Obra.objects.get(pk=id)
    except Obra.DoesNotExist:
        return Response({"mensagem": "Obra não encontrada"}, status=status.HTTP_404_NOT_FOUND)  
    
    if request.method == 'GET':
        serializer = ObraSerializer(obra)
        return Response(serializer.data)
    if request.method == 'DELETE':
        obra.delete()
        return Response({"mensagem": "Obra deletada!"})
    
  
 
@api_view(['GET', 'DELETE'])
def atordublador_detalhe(request, id):
    try:
        atordublador = AtorDublador.objects.get(pk=id)
    except AtorDublador.DoesNotExist:
        return Response({"mensagem": "Ator/Dublador não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AtorDubladorSerializer(atordublador)
        return Response(serializer.data)
    if request.method == 'DELETE':
        atordublador.delete()
        return Response({"mensagem": "Ator/Dublador deletado!"})

 
@api_view(['GET' 'DELETE'])
def personagem_detalhe(request, id):
    try:
        personagem = Personagem.objects.get(pk=id)
    except Personagem.DoesNotExist:
        return Response({"mensagem": "Personagem não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PersonagemSerializer(personagem)
        return Response(serializer.data)
    if request.method == 'DELETE':
        personagem.delete()
        return Response({"mensagem": "Personagem deletado!"})
  
 
@api_view(['GET' 'DELETE'])
def habilidade_detalhe(request, id):
    try:
        habilidade = Habilidade.objects.get(pk=id)
    except Habilidade.DoesNotExist:
        return Response({"mensagem": "Habilidade não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = HabilidadeSerializer(habilidade)
        return Response(serializer.data)
    if request.method == 'DELETE':
        habilidade.delete()
        return Response({"mensagem": "Habilidade deletada!"})
  
 
@api_view(['GET' 'DELETE'])
def relacionamento_detalhe(request, id):
    try: 
        relacionamento = Relacionamento.objects.get(pk=id)
    except Relacionamento.DoesNotExist:
        return Response({"mensagem": "Relacionamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RelacionamentoSerializer(relacionamento)
        return Response(serializer.data)
    if request.method == 'DELETE':
        relacionamento.delete()
        return Response({"mensagem": "Relacionamento deletado!"})

   
 
@api_view(['GET' 'DELETE'])
def personagemhabilidade_detalhe(request, id):
    try:
        personagemhabilidade_detalhe = PersonagemHabilidade.objects.get(pk=id)
    except PersonagemHabilidade.DoesNotExist:
        return Response({"mensagem": "PersonagemHabilidade não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonagemHabilidadeSerializer(personagemhabilidade_detalhe)
        return Response(serializer.data)  
    if request.method == 'DELETE':
        personagemhabilidade_detalhe.delete()
        return Response({"mensagem": "PersonagemHabilidade deletada!"})

@api_view(['DELETE'])
def deletar_obra(request, id):
    try:
        obra = Obra.objects.get(pk=id)
    except Obra.DoesNotExist:
        return Response({"mensagem": "Obra não encontrada"})
    
    obra.delete()
    return Response({"mensagem": "Obra deletada!"})



@api_view(['GET''DELETE'])
def deletar_personagem(request, id):
    try:
        personagem = Personagem.objects.get(pk=id)
    except Personagem.DoesNotExist:
        return Response({"mensagem": "Personagem não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PersonagemSerializer(personagem)
        return Response(serializer.data)
    if request.method == 'DELETE':
        personagem.delete()
        return Response({"mensagem": "Personagem deletado!"})

   