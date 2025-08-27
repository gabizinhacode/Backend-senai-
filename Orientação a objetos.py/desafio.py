# Sistema para organizar áreas importantes da indústria

# ------------------------------
# Classe Carro
# ------------------------------
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def detalhes(self):
        print("-------------------")
        print("Detalhes do Veículo")
        print("-------------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-------------------")

# ------------------------------
# Classe Pessoa
# ------------------------------
class Pessoa:
    def __init__(self, nome, cargo, matricula):
        self.nome = nome
        self.cargo = cargo
        self.matricula = matricula

    def detalhes(self):
        print("-------------------")
        print("Dados do Funcionário")
        print("-------------------")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Matrícula: {self.matricula}")
        print("-------------------")

# ------------------------------
# Classe Manual
# ------------------------------
class Manual:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado

    def informacoes(self):
        print("-------------------")
        print("Manual Técnico")
        print("-------------------")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano Publicado: {self.ano_publicado}")
        print("-------------------")

# ------------------------------
# Classe Produto
# ------------------------------
class Produto:
    def __init__(self, nome, quantidade, codigo):
        self.nome = nome
        self.quantidade = quantidade
        self.codigo = codigo

    def detalhes(self):
        print("-------------------")
        print("Produto em Estoque")
        print("-------------------")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Código: {self.codigo}")
        print("-------------------")

# ------------------------------
# Classe Treinamento
# ------------------------------
class Treinamento:
    def __init__(self, nome, data, duracao, obrigatorio=True):
        self.nome = nome
        self.data = data
        self.duracao = duracao
        self.obrigatorio = obrigatorio

    def detalhes(self):
        print("-------------------")
        print("Treinamento")
        print("-------------------")
        print(f"Nome: {self.nome}")
        print(f"Data: {self.data}")
        print(f"Duração: {self.duracao} horas")
        print(f"Status: {'Obrigatório' if self.obrigatorio else 'Opcional'}")
        print("-------------------")

# ------------------------------
# Classe Aluno
# ------------------------------
class Aluno:
    def __init__(self, nome, curso, nota):
        self.nome = nome
        self.curso = curso
        self.nota = nota

    def detalhes(self):
        print("-------------------")
        print("Aluno em Capacitação")
        print("-------------------")
        print(f"Nome: {self.nome}")
        print(f"Curso: {self.curso}")
        print(f"Nota: {self.nota}")
        print(f"Resultado: {'Aprovado ✅' if self.nota >= 7 else 'Reprovado ❌'}")
        print("-------------------")

# ------------------------------
# Simulação dos cadastros
# ------------------------------

# Frota de Veículos
print("\n==== Frota de Veículos ====")
carro1 = Carro("Volkswagen", "Delivery", 2020)
carro2 = Carro("Mercedes", "Sprinter", 2021)
carro1.detalhes()
carro2.detalhes()

# Funcionários
print("\n==== Funcionários ====")
func1 = Pessoa("Erick", "Operador", 101)
func2 = Pessoa("Gabriela", "Engenheira", 102)
func3 = Pessoa("Junior", "Técnico", 103)
func1.detalhes()
func2.detalhes()
func3.detalhes()

# Manuais Técnicos
print("\n==== Manuais Técnicos ====")
manual1 = Manual("Prensa Hidráulica", "Carlos Silva", 2022)
manual2 = Manual("Esteira Transportadora", "Ana Souza", 2021)
manual1.informacoes()
manual2.informacoes()

# Produtos em Estoque
print("\n==== Produtos em Estoque ====")
prod1 = Produto("Parafuso M10", 500, "P001")
prod2 = Produto("Rolamento 6204", 120, "P002")
prod3 = Produto("Correia A32", 45, "P003")
prod1.detalhes()
prod2.detalhes()
prod3.detalhes()

# Treinamentos Obrigatórios
print("\n==== Treinamentos ====")
trein1 = Treinamento("Python básico", "10/09/2025", 8, obrigatorio=False)
trein2 = Treinamento("Brigada de Incêndio", "15/09/2025", 4, obrigatorio=True)
trein1.detalhes()
trein2.detalhes()

# Cursos de Capacitação
print("\n==== Cursos de Capacitação ====")
aluno1 = Aluno("Ariana Lima", "Excel Avançado", 9)
aluno2 = Aluno("Pedro Alves", "Gestão Produção", 6)
aluno3 = Aluno("Lucas Martins", "Manutenção Mecânica", 7.5)
aluno1.detalhes()
aluno2.detalhes()
aluno3.detalhes()
