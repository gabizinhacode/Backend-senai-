#Peça um número inteiro e mostre sua representação em binário (sem usar bin()).

numero = int(input("Digite um número inteiro: "))
binario = ""

if numero == 0:
    binario = "0"
else:
    n = numero
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2

print(f"O número {numero} em binário é: {binario}")

