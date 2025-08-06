#Peça ao usuário para digitar quantas notas quiser (digite -1 para encerrar). Calcule e mostre a media das notas digitadas.
notas =[]
while True:
    nota = float (input("digite uma nota (ou -1 para sair):"))
    if nota == -1:
        break
    notas.append(nota)

    if notas:
        media = sum(notas) / len (notas)
        print(f"a media das notas digitads é:", media)
    else:
        print("Nenhuma nota foi digitada.")
