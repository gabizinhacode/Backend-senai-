#Crie uma classe chamada pessoa, com os atributos nome, idade, setor onde cada funcionario atua como produção, qualidade, manuntenção, e um metodo chamado apresentar() que exibda uma mensagem apresentando o colaborador
class Pessoa: 
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor 

    def apresentar(self):
            print("-------------------")
            print(f"Nome: {self.nome}")
            print(f"Idade: {self.idade}")
            print(f"Setor: {self.setor}")
            print("-------------------")
            print("Prazer em conhecê-lo!")
            print("-------------------")
pessoa1 = Pessoa("erick", 30, "Produção")
pessoa1.apresentar()
pessoa2 = Pessoa("gabi", 25, "Qualidade")
pessoa2.apresentar()
pessoa3 = Pessoa("erick junior", 28, "Manuntenção")
pessoa3.apresentar()
