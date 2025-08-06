#. Simule o lançamento de dois dados até que a soma seja 7. Mostre quantas tentativas foram necessárias.

import random

tentativas = 0

while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    tentativas += 1
    if dado1 + dado2 == 7:
        break

print(f"Foram necessárias {tentativas} tentativas para obter soma igual a 7.")
