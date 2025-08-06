# Simule um sistema de login. A senha correta é "1234". Enquanto o usuário não digitar a senha certa, continue pedindo
while True:
    senha = input("digite a senha:")
    if senha == "1234":
        print("senha correta, bem vindo ao sistema")
        break
    else:
        print("senha incorreta, tente novamente")


