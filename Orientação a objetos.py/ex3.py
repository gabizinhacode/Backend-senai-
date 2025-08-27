#Crie uma classe chamada manual, com esses atributos titulo, autor, ano de publicação para que os tecnicos saibam se estao consultando documentos atualizados e um metodo chamado informações() que mostre os dados no formato "O manual [titulo], escrito por [autor], foi publicado em [ano de publicação]"
class Manual:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado

    def informacoes(self):
        print(f"O manual {self.titulo}, escrito por {self.autor}, foi publicado em {self.ano_publicado}")

manual1 = Manual("de python", "Guido van Rossum", 2021)
manual1.informacoes()

