# Peça 10 números ao usuário e diga quantos deles são positivos.
positivos = 0
for i in range(10):
    number = int(input("digite um numero:"))
    if number > 0:
        positivos += 1
        print (f" voce digitou {positivos} positive numbers:")
