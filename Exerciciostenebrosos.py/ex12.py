#conversão de binario para decimal: crie uma função chamada binario_para_decimal que recebe uma string representado um numero binario como parametro e retorna True se o numero for impar e False caso o contrario 
def binario_para_decimal(binario):
    numero = binario[::-1]  
    potencia = 0
    soma = 0
    for i in numero:
        soma += int(i) * (2 ** potencia)
        potencia += 1
    return soma % 2 == 1

binario = input("Digite um número binário: ")
print(binario_para_decimal(binario))    
