from django.db import models
 
# Create your models here.
class Obra(models.Model):
 
 
    TIPO_CHOICES = [
        ('Anime', 'ANIME'),
        ('Filme', 'FILME'),
        ('Serie', 'SERIE'),
        ('Livro', 'LIVRO'),
       
    ]
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=5, choices=TIPO_CHOICES)
    ano_lancamento = models.DateField(null=True, blank=True)
    estudio_produtora = models.CharField(max_length=100)
 
    def __str__(self):
        return self.titulo
   
class AtorDublador(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)
    data_nascimento = models.DateField()
 
    def __str__(self):
        return self.nome
 
 
class Personagem(models.Model):
 
    GENERO_CHOICES = [
    ('M', 'Mulher'),
    ('H', 'HOMEM'),
    ('O', 'Outro')
]
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    genero = models.CharField(max_length=5, choices=GENERO_CHOICES)
    especie = models.CharField(max_length=50)
    descricao = models.TextField()
    ator_dublador = models.ForeignKey(AtorDublador, on_delete=models.SET_NULL, null=True)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.nome} - {self.ator_dublador}'
   
class Habilidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
 
    def __str__(self):
        return self.nome
   
class Relacionamento(models.Model):
 
    TIPO_CHOICES = [
    ('amigo', 'Amigo'),
    ('Aliado', 'Aliado'),
    ('inimigo', 'Inimigo'),
    ('parente', 'Parente')
]
    personagem_origem = models.ForeignKey(Personagem, on_delete=models.CASCADE, related_name='relacionamentos_de_origem')
    personagem_destino = models.ForeignKey(Personagem, on_delete=models.CASCADE, related_name='relacionamentos_de_destino')
    tipo_relacionamento = models.CharField(max_length=20,choices=TIPO_CHOICES)
 
    def __str__(self):
        return f" {self.tipo_relacionamento} "
   
class PersonagemHabilidade(models.Model):
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE, related_name='personagem')
    habilidade = models.ForeignKey(Habilidade, on_delete=models.CASCADE, related_name='habilidade')
 
    def __str__(self):
        return f"{self.personagem} - {self.habilidade}"
 