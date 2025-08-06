# Peça um número ao usuário e imprima a tabuada desse número de 1 a 10
number = int (input("digite um numero:"))
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")
    