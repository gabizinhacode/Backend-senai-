class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20

funcionario = Funcionario("João", 3000)
gerente = Gerente("erick", 5000)

print(f"Bônus do funcionário {funcionario.nome}: R$ {funcionario.calcular_bonus():.2f}")
print(f"Bônus do gerente {gerente.nome}: R$ {gerente.calcular_bonus():.2f}")

