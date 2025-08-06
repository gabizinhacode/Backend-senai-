#Peça um número ao usuário e diga se ele é perfeito (a soma de seus divisores próprios é igual ao número)

numero = int(input("Digite um número: "))
soma = 0

for i in range(1, numero):
    if numero % i == 0:
        soma += i

if soma == numero:
    print(f"{numero} é um número perfeito")
else:
    print(f"{numero} não é um número perfeito")