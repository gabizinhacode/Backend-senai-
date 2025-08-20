#calculo do numero de digitos: crie uma função chamada numero_digitos que recebe um inteiro positivo como parametro e retorna o numero de digitos presentes nesse numero 
def numero_digitos(numero):
    if numero < 0:
        raise ValueError("o numero deve ser inteiro e positivo")
    if numero == 0:
        return 1
    
    return len(str(numero))
  
numero = int(input("digite um numero inteiro positivo: "))
resultado = numero_digitos(numero)
print(f"o numero de digitos é: {resultado}")