#programa que recebe 5 notas de alunos e verifique se a media é maior ou a igual a 5 (aprovado) se a media for entre 2.5 e 5 (recuperação) e se a media for menor que 2.5 (reprovado)
notas = []
soma = 0
for i in range(5):
    nota = float(input("digite a nota do aluno:"))
    soma = soma + nota
media = soma / 5
if media >= 5:
    print("Aprovado")
elif 2.5 <= media < 5:
    print("Recuperação")
elif media < 2.5:
    print("Reprovado")
soma = 0
print(f"A média das notas é: {media:.2f}")





        


