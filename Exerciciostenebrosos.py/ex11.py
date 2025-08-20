#Calculo da hipotenusa de um triangulo retangulo: crie uma função chamada hipotenusa que recebe os catetos de um triangulo retangulo como parametros e retorna a hipotenusa do triangulo 
def hipotenusa(cateto1, cateto2):
    if cateto1 <= 0 or cateto2 <=0:
        raise ValueError("os catetos devem ser numeros positivos")
    return (cateto1 ** 2 + cateto2 ** 2) ** 0.5

cateto1 = float(input("digite o valor do primeiro cateto:"))
cateto2 = float(input("digite o valor do segundo cateto:"))

resultado = hipotenusa(cateto1, cateto2)
print(f"a hipotenusa do triangulo retangulo é: {resultado:.2f}") 