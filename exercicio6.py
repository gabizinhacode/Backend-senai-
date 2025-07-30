#programa que solicite numeros até o usuario digitar um numero negativo, e verifique qual dos numeros digitados é o maior 
numero = int(input("Digite um número (negativo para sair): "))

if numero < 0:
    print("Nenhum número foi digitado.")
else:
    maior = numero
    while True:
        numero = int(input("Digite um número (negativo para sair): "))
        if numero < 0:
            break
        if numero > maior:
            maior = numero
    print("O maior número digitado foi:", maior)