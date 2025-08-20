#gerador de numeros aleatorios: crie uma função chamada gerar_numeros_aleatorios que recebe um inteiro positivo n e m e retorne um numero aleatório entre n e m
import random

def gerar_numeros_aleatorios(n, m):
    if n >= m:
        raise ValueError("n deve ser menor que m")
    return random.randint(n,m)

n = int(input("digite o valor de n:"))
m = int(input("digite o valor de m:"))
resultado = gerar_numeros_aleatorios(n,m)
print(f"número aleatório entre {n} e {m}: {resultado}")

