# Calculo do imc: crie um,a função chamada calcular_imc que recebe peso e altura de uma pessoa como parametros e retorna o indice da massa corporal dessa pessoa
def calcular_imc(peso, altura): 
    if altura <= 0:
        raise ValueError("a altura deve ser maior que zero")
    if peso <=0:
        raise ValueError("o peso deve ser maior que zero")
    imc = peso / (altura ** 2)
    return imc 
peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))
resultado = calcular_imc(peso, altura)
print(f"seu imc é: {resultado:.2f}")