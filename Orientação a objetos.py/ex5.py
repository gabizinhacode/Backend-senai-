#crie uma classe chamada treinamento, com esses atributos titulo, instrutor e a duração em minutos e um metodo chamdo descricao() que exiba as informações organizadas 
class Treinamento:
    def __init__(self, titulo, instrutor, duracao):
        self.titulo = titulo
        self.instrutor = instrutor
        self.duracao = duracao

    def descricao(self): 
            print("-------------------")
            print("Detalhes do treinamento:")
            print("-------------------")
            print(f"Título: {self.titulo}")
            print(f"Instrutor: {self.instrutor}")
            print(f"Duração: {self.duracao} minutos")
            print("-------------------")
treinamento1 = Treinamento("Python Básico", "Gabriela", 120)
treinamento1.descricao()