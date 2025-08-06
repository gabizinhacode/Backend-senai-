#Leia 5 números e mostre o maior e o menor digitado
numeros = []
for i in range(5):
    numero = int(input("digite um numero:"))
    numeros.append(numero)

    print(" o maior numero digitado foi:", max(numeros))
    print(" o menor numero digitado foi:", min(numeros))