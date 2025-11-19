from rest_framework.decorators import api_view
from .models import Obra, AtorDublador, Personagem, Habilidade, Relacionamento, PersonagemHabilidade
from .serializers import ObraSerializer, AtorDubladorSerializer, PersonagemSerializer, HabilidadeSerializer, RelacionamentoSerializer, PersonagemHabilidadeSerializer
from rest_framework.response import Response
from rest_framework import status
 
@api_view(['GET'])
def obra_detalhe(request, id):
    obra = Obra.objects.get(pk=id)
    serializer = ObraSerializer(obra)
    return Response(serializer.data)
 
@api_view(['GET'])
def atordublador_detalhe(request, id):
   atordublador = AtorDublador.objects.get(pk=id)
   serializer = AtorDubladorSerializer(atordublador)
   return Response(serializer.data)
 
@api_view(['GET'])
def personagem_detalhe(request, id):
   personagem = Personagem.objects.get(pk=id)
   serializer = PersonagemSerializer(personagem)
   return Response(serializer.data)
 
@api_view(['GET'])
def habilidade_detalhe(request, id):
   habilidade = Habilidade.objects.get(pk=id)
   serializer = HabilidadeSerializer(habilidade)
   return Response(serializer.data)
 
@api_view(['GET'])
def relacionamento_detalhe(request, id):
   relacionamento = Relacionamento.objects.get(pk=id)
   serializer = RelacionamentoSerializer(relacionamento)
   return Response(serializer.data)
 
@api_view(['GET'])
def personagemhabilidade_detalhe(request, id):
   personagemhabilidade = PersonagemHabilidade.objects.get(pk=id)
   serializer = PersonagemHabilidadeSerializer(personagemhabilidade)
   return Response(serializer.data)