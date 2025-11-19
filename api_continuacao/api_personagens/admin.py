from django.contrib import admin
from .models import Obra, Personagem, AtorDublador, Habilidade, Relacionamento, PersonagemHabilidade
# Register your models here.
 
admin.site.register(Obra)
admin.site.register(Personagem)
admin.site.register(AtorDublador)
admin.site.register(Habilidade)
admin.site.register(Relacionamento)
admin.site.register(PersonagemHabilidade)