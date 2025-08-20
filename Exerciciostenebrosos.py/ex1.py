#conversão de decimal para binário: crie uma função chamada decimal_para_binario que recebe um numero inteiro positivo com parametro e retorna a representação binaria desse numero como uma string
def decimal_para_binario(numero):
    if numero < 0:
        raise ValueError("o numero deve ser inteiro e positivo")
    if numero == 0: 
        return "0"
    
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario
    
numero = int(input("Digite um número inteiro positivo: "))
print("Binário:", decimal_para_binario(numero))
    


    
    
