# Peça uma palavra e diga se ela é um palíndromo (ex: "radar", "ana")

palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo!")