#jogo de advinhação inteligente: crie uma função chamda jogar_adivinhação que implementa um jogo de adivinhação. O computador deve escolher um numero aleatorio entre 1 e 100. o jogador tem 10 tentativas para adivinhar o numero. A cada tentativa, o programa deve informar se o numero digitado é maior ou mneor que o numero secreto. Se o jogador acertar, o programa deve exibir uma mensagem de parabens e informar o numero de tenativas que ele utilizou, A função deve implementar uma "dica inteligente" para o jogador. Se o jogador errar, a função deve sugerir um intervalo menor para o proximopalpite (por exemplo, "o numero esta entre 50 e 70")
import random
def jogar_adivinhação():
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    baixo = 1
    alto = 100

    print("Bem-vindo ao jogo de adivinhação!")
    print("tente adivinhar o numero entre 1 e 100")
    print(f"você tem {max_tentativas} tentativas")

    while tentativas < max_tentativas:
        print(f"tentativa {tentativas + 1} de {max_tentativas}")
        palpite = int(input("Digite seu palpite: "))

        if palpite < baixo or palpite > alto:
            print(f"Por favor, digite um número entre {baixo} e {alto}.")
            continue
        tentativas += 1
        if palpite < numero_secreto:
            print("Muito baixo!")   
            baixo = max(baixo, palpite + 1)
            print(f"Tente um número entre {baixo} e {alto}.")
        elif palpite > numero_secreto:
            print("Muito alto!")
            alto = min(alto, palpite - 1)
            print(f"Tente um número entre {baixo} e {alto}.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

    if tentativas == max_tentativas:
        print(f"Você não conseguiu adivinhar o número. O número era {numero_secreto}.")

jogar_adivinhação()