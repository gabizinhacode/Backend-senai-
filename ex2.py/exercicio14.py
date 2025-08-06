#. Peça um número n e mostre os n primeiros termos da sequência de Fibonaci
n = int(input("Digite o número de termos: "))

a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b