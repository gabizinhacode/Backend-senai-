from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=70)
    isbn = models.IntegerField(unique=True)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.titulo} - {self.isbn} - {self.descricao}"

class Autor(models.Model):
    nome = models.CharField(max_length=70)
    data_nascimento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.data_nascimento} - {self.biografia}"

class Usuario(models.Model):
    nome = models.CharField(max_length=70)
    numero_identificacao = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField(auto_now_add=True)
    nivel_associacao = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome} - {self.nivel_associacao} - {self.email} - {self.data_cadastro} - {self.numero_identificacao} - {self.nivel_associacao}"

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_categoria
    
class Emprestimo(models.Model):
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_devolucao = models.DateField()
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao_limite = models.DateField()

    def __str__(self):
        return f"{self.id_livro} - {self.id_usuario} - {self.data_emprestimo} - {self.data_devolucao} - {self.data_devolucao_limite}"

class livro_autor(models.Model):
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_livro} - {self.id_autor}"

class livro_categoria(models.Model):
    id_livro= models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id_livro} - {self.id_categoria}"
    

