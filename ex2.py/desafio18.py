#Peça um valor e calcule a quantidade mínima de cédulas (100, 50, 20, 10, 5, 2, 1) para esse valor

valor = int(input("Digite o valor: "))
cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    qtd = valor // cedula
    if qtd > 0:
        print(f"{qtd} cédula(s) de {cedula}")
        valor = valor % cedula
