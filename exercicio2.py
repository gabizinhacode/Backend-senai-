#programa que leia o ano de nascimento do usuario, o nome e diga ao usuario qual a idade dele em 2025
ano_nascimento = int(input("Digite o ano de nascimento: "))
nome = input("Digite o seu nome: ")
idade = 2025 - ano_nascimento   
print(f"{nome}, você terá {idade} anos em 2025.")