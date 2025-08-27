#crie uma classe chamada aluno, com os atributos nome do aluno, curso e a nota final, o sistema deve mostrar se o aluno esta aprovado  (nota >7) ou (nota < 7) e um metodo chamado status() que exiba o nome do aluno, o curso, e o resultado (aprovado ou reprovado)
class Aluno:
    def __init__(self, nome, curso, nota):
        self.nome = nome 
        self.curso = curso
        self.nota = nota 

    def status(self):
            if self.nota > 7:
                resultado = "Aprovado"
            else:
                resultado = "Reprovado"
            print(f"Nome: {self.nome}")
            print(f"Curso: {self.curso}")
            print(f"Status: {resultado}")
aluno1 = Aluno("Erick", "Python", 8)
aluno1.status()
