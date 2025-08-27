#crie uma classe chamada carro, com os atributos marca, modelo e o ano e um metodo chamado detalhes(), que exba as informações do veiculo de forma organizada
class Carro:
    def __init__(self,marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def detalhes(self):
        print("-------------------")
        print("Detalhes do veículo:")
        print("-------------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-------------------")

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = int(input("Digite o ano do carro: "))

carro1 = Carro(marca, modelo, ano)
carro1.detalhes()

