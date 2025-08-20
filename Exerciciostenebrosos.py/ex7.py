#calculo do volume do cilindro: crie uma função chamada volume_cilindro que recebe o raio da base e a altura de um cilindro como parametros e retorna o volume do cilindro 
def volume_cilindro(raio, altura):
    if raio <= 0 or altura <= 0:
        raise ValueError("o raio e a altura devem ser maiores que zero")
    return 3.14 * raio ** 2 * altura

raio = float(input("digite o raio da base do cilindro: "))
altura = float(input("digite a altura do cilindro:"))

resultado = volume_cilindro (raio, altura)
print(f"o volume do cilindro é: {resultado:.2f}")



