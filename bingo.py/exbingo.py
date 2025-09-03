import random
import pyttsx3
from pyfiglet import figlet_format
import msvcrt
import time

class Bingo:
    def __init__(self):
        # Intervalos de cada letra
        self.letras = {
            'B': list(range(1, 16)),
            'I': list(range(16, 31)),
            'N': list(range(31, 46)),
            'G': list(range(46, 61)),
            'O': list(range(61, 76))
        }
        self.sorteados = set()  # Guardar os números que já saíram
    
    # Sorteia e retorna uma letra entre ('B','I','N','G','O')
    def sortear_letra(self):
        return random.choice(list(self.letras.keys()))

    # Dado uma letra, sorteia e retorna um número possível
    def sortear_numero(self, letra):
        numeros_possiveis = self.letras[letra]
        while True:
            numero = random.choice(numeros_possiveis)
            if (letra, numero) not in self.sorteados:
                self.sorteados.add((letra, numero))
                return numero
            # Se já foi sorteado, continua tentando

    # Utilizando as funções de sortear letra e número
    def sorteio(self):
        if len(self.sorteados) >= 75:
            return "Todos os números já foram sorteados!"
        letra = self.sortear_letra()
        numero = self.sortear_numero(letra)
        return f"{letra}{numero}"

    # Se necessário pode criar outras funções auxiliares
    def jogar(self):
        print(figlet_format("BINGO", font="standard"))
        while True:
            print("Sorteando em 3")
            time.sleep(1)
            print("Sorteando em 2")
            time.sleep(1)
            print("Sorteando em 1")
            time.sleep(1)
            sorteio = self.sorteio()
            self.falar(sorteio)
            time.sleep(3)
            print(sorteio)
            msvcrt.getch()

    # Não mexer nessas abaixo
    def falar(self, texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()


bingo = Bingo()
bingo.jogar()

