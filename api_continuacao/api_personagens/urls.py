from django.urls import path, include
from .views import obra_detalhe, atordublador_detalhe, personagem_detalhe, habilidade_detalhe, relacionamento_detalhe, personagemhabilidade_detalhe
 
urlpatterns = [
    path('obra/<int:id>/', obra_detalhe, name='obra_detalhe'),
    path('ator/<int:id>/', atordublador_detalhe, name='atordublador_detalhe'),
    path('personagem/<int:id>/', personagem_detalhe, name='personagem_detalhe'),
    path('habilidade/<int:id>/', habilidade_detalhe, name='habilidade_detalhe'),
    path('relacionamento/<int:id>/', relacionamento_detalhe, name='relacionamento_detalhe'),
    path('personagemhabilidade/<int:id>/', personagemhabilidade_detalhe, name='personagemhabilidade_detalhe'),
]