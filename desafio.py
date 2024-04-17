saldo = 0
quantidade_saques = 0
LIMITE_SAQUE = 500.0
MAX_SAQUES = 3
extrato = ""
MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """


print("Seja bem vindo!")
while True:
    print("Informe a operação desejada.")
    opcao = input(MENU)
    if opcao.upper() == "X":
        print("Obrigado por sua preferencia.")
        break
    elif opcao.upper() == "D":
        deposito = float(input("Informe a quantia que deseja depósitar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("Falha! O valor informado é inválido.")
    elif opcao.upper() == "S":
        valor = float(input("Informe a quantia que deseja sacar: "))
        if valor > saldo:
            print("Falha! Saldo insuficiente.")

        elif valor > LIMITE_SAQUE:
            print("Falha! O valor do saque excede o limite.")

        elif quantidade_saques >= MAX_SAQUES:
            print("Falha! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saques += 1

        else:
            print("Falha! O valor informado é inválido.")

    elif opcao.upper() == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    else:
        print("Opção inválida!")
        print("Por favor selecione novamente a operação desejada!")
        print()
