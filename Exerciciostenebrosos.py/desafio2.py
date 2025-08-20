#simulador de banco: crie uma função chamada simular_banco que simula um sistema bancario simples. A função deve permitir que o usuario faça operações como: criar uma nova conta (com nome, saldo inicial), deposiatr dinheiro em uma conta exsistente, sacar dinheiro de uma conta existente, exibir o saldo de uma conta, sair do sistema. Implemente a função utilizando estruturas como listas ou dicionarios para armazenar as informações das contas. Utilize funções auxiliares para organizar as diferentes operações do sistema bancario. A função deve ser capaz de tratar erros como saldo insuficiente, conta inexistente, etc. 
def simular_banco():
    contas = {}

    def criar_conta():
        nome = input("digite seu nome:")
        if nome in contas:
            print("conta ja existente!")
            return 
        saldo = float(input("digite o saldo inicial:"))
        contas[nome] = saldo
        print("conta criada com sucesso!!")

    def depositar():
        nome = input("digite o nome da conta:")
        if nome not in contas:
            print("conta não encontrada.")
            return 
        valor = float(input("valor do deposito:"))
        contas[nome] += valor
        print("deposito realizado com sucesso!")

    def sacar():
        nome = input("digite o nome da conta:")
        if nome not in contas:
           print("conta não encontrada.")
           return 
        valor = float(input("valor do saque: "))
        if  contas[nome] >= valor:
            print("saque realizado com sucesso!")
        else:
            contas[nome] -= valor
            print("saldo insuficiente.")

    def exibir_saldo():
        nome = input("digite o nome da conta:")
        if nome not in contas:
           print(f"saldo de {nome}: R$ {contas[nome]:.2f}")
        else: 
            print("conta não encontrada")                        
    while True:
          print("\n--- Menu Banco ---")
          print("1. criar conta")
          print("2. depositar")
          print("3. sacar")
          print("4. exibir saldo")
          print("5. sair")
          opcao = input("escolha uma opção: ")
          if opcao == "1":
              criar_conta()
          elif opcao == "2":
               depositar()
          elif opcao == "3":
                sacar()
          elif opcao == "4":
                exibir_saldo()
          elif opcao == "5":
               print("saindo...")
               break
          else:
              print("opção inválida.")
simular_banco()