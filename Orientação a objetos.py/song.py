import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def digitar(texto, cor=Fore.WHITE, velocidade=0.07):
    for letra in texto:
        sys.stdout.write(cor + letra + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()


frases = [
    (0, Fore.CYAN, "Antes de você, eu não sabia o que era o amor"),
    (3, Fore.GREEN, "Você me amou primeiro..."),
    (10, Fore.YELLOW, "Antes que houvesse dia"),
    (6, Fore.MAGENTA, "Antes que houvesse noite"),
    (8, Fore.RED, "Antes que o tempo pudesse ser contado"),
    (9, Fore.CYAN, "Você já me amava!"),
    (4, Fore.GREEN, "E eu já era objeto das suas afeições")
]

inicio = time.time()
for tempo, cor, frase in frases:
 
    while time.time() - inicio < tempo:
        time.sleep(0.1)
    digitar(frase, cor, 0.05)

print()
digitar("  Antes de Você - José Jr.", Fore.LIGHTBLACK_EX, 0.05)



