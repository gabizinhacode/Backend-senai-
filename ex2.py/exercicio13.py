#Peça ao usuário um número n e desenhe um triângulo com n linhas, assim: ***

n = int(input("Digite o número de linhas: "))

for i in range(1, n + 1):
    print('*' * i)


