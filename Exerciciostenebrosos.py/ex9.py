#calculo da area do retangulo: crie uma função chamada area_retangulo que a base e a altura de um retangulo como parametros e retorna a area do retangulo 
def area_retangulo(base, altura):
    if base < 0 or altura < 0:
        raise ValueError("a base e a altura devem ser numeros positivos")
    return base * altura

base = float(input("digite a base do retangulo: "))
altura = float(input("digite a altura do retangulo: "))

resultado = area_retangulo(base, altura)
print(f"a area do retangulo é: {resultado:.2f}")
