#Utilizando a biblioteca time, crie um relogio, a hora pode começar das 00:00 
import time
hora = 0
minuto = 0
segundo = 0
while True:
    print(f"{hora:02}:{minuto:02}:{segundo:02}", end='\r')
    time.sleep(1)
    segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
    if minuto == 60:
        minuto = 0
        hora += 1
    if hora == 24:
        hora = 0