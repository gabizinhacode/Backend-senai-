#calculo do raio de um circulo: crie uma função chamada raio_circulo que recebe a area de um circulo como parametro e retorna o raio desse circulo
def raio_circulo(area):
    if area < 0:
        raise ValueError("a area deve ser maior que zero")
    raio = (area / 3.14) ** 0.5
    return raio

area = float(input("digite a area do circulo:"))
resultado = raio_circulo(area)
print(f"o raio do circulo é: {resultado:.2f}")

