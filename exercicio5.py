#programa que receba um numero inteiro positivo e exibe uma contagem de 0 ate o numero lido
numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print("Contagem de 0 até", numero)
    for i in range(numero + 1):
        print(i, end=' ')
    print()
    