# O computador escolhe um número de 1 a 100. O usuário deve adivinhar. Dê dicas ("maior" ou "menor") até acertar

import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Tente adivinhar o número (entre 1 e 100): "))
    if palpite < numero_secreto:
        print("Maior!")
    elif palpite > numero_secreto:
        print("Menor!")
    else:
        print("Parabéns! Você acertou o número!")
