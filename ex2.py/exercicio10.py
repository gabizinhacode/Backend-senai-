# Peça um número ao usuário e diga se ele é primo
numero = int(input("digite um numero:"))
eh_primo = True 

if numero < 2:
    eh_primo = False 
else: 
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False 
            break

if eh_primo:
    print(f"{numero} é um numero primo")
else:
    print(f"{numero} não é um numero primo")


