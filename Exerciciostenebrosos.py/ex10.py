#calculo da area de um circulo: crie uma função chamada area_circulo que recebe o raio de um circulo como parametro e retorna a area do circulo
def area_circulo(raio):
    if raio < 0:
        raise ValueError("o raio deve ser um numero positivo")
    return 3.14 * raio ** 2

raio = float(input("digite o raio do circulo: "))

resultado = area_circulo(raio)
print(f"a area do circulo é: {resultado:.2f}")
