from .models import Obra, AtorDublador, Personagem, Habilidade, Relacionamento, PersonagemHabilidade
from rest_framework import serializers
 
 
class AtorDubladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtorDublador
        fields = '__all__'
        read_only_fields = ['id']
 
 
class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'
        read_only_fields = ['id']
 
class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = '__all__'
        read_only_fields = ['id']
 
class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = '__all__'
        ready_only_fields = ['id']
 
class RelacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacionamento
        fields = '__all__'
        ready_only_fields = ['id']
 
class PersonagemHabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonagemHabilidade
        fields = '__all__'
        ready_only_fields = ['id']