class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
            def __init__(self, marca, modelo, quantidade_de_portas):
                super().__init__(marca, modelo)
                self.quantidade_de_portas = quantidade_de_portas

            def exibir_dados(self):
                    print(f"Marca: {self.marca}")
                    print(f"Modelo: {self.modelo}")
                    print(f"Quantidade de portas: {self.quantidade_de_portas}")

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
porta = int(input("Digite a quantidade de portas do carro: "))

carro1 = Carro(marca,modelo,porta)
carro1.exibir_dados()