#
def distancia_pontos (x1,x2,y1,y2):
    x2_menos_x1 = x2 - x1
    y2_menos_y1 = y2 - y1 

    x_quadrado = x2_menos_x1 ** 2
    y_quadrado = y2_menos_y1 ** 2

    soma = x_quadrado + y_quadrado
    distancia = soma ** 0.5
    return distancia

x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))

y1 = float(input("Digite o valor de y1: "))
y2 = float(input("Digite o valor de y2: "))

resultado = distancia_pontos(x1, y1, x2, y2)
print(resultado) 

