#jogo da forca onde a palavra é escolhida, vem de uma palavra de uma lista de palavra (list)
palavras = ["gabi", "linda", "maravilhosa", "magnifica", "inteligente"]
import random
palavra = random.choice(palavras)
letras_acertadas = []
tentativas = 6

while tentativas > 0:
    exibir = ""
    for letra in palavra:
        if letra in letras_acertadas:
            exibir += letra
        else:
            exibir += "_"
    print("palavra:", exibir)

    if "_" not in exibir:
        print("parabens, voce acertou a palavra!")
        break

    chute = input("digite uma letra:")
    if chute in letras_acertadas:
        print("voce ja chutou essa letra, tente novamente")
        continue
    if chute in palavra:
        letras_acertadas.append(chute)
        print("Uhuuul, você acertou uma letra!")
    else:
        tentativas -= 1
        print("ops, você errou! Você ainda tem", tentativas, "tentativas.")

if tentativas == 0:
    print("que pena, você perdeu! A palavra era:", palavra)