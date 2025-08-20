#calculo da area de um quadrado: crie uma função chamada area_quadrado  que recebe o lado de um quadrado como parametro e retorna a area do quadrado 
def area_quadrado(lado):
    if lado < 0:
        raise ValueError("o lado deve ser um numero positivo")
    return lado ** 2 

lado = float(input("digite o lado do quadrado:"))
resultado = area_quadrado(lado) 

print(f"a area do quadrado é: {resultado:.2f}")

