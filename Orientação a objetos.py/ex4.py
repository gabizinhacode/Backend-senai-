#crie uma classe chamado produto, com esses atributos nome do produto, preço unitario e quantidade disponivel e um metodo chamdo mostrar_estoque() que exiba os dados no formato "Produto: [nome]/ preco: R$[preco]/ Quantidade em estoque: [quantidade]"
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_estoque(self):
        print(f"Produto: {self.nome}/ preco: R${self.preco}/ Quantidade em estoque: {self.quantidade}")
produto1 = Produto("Notebook", 3500.00, 10)
produto1.mostrar_estoque()
