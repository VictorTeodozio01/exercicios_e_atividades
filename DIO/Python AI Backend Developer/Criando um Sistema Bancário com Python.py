menu = """
[1] Sacar
[2] Depositar
[3] Visualizar Extrato

Selecione uma opção: """

limite = 500
saldo = 0
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao_do_menu = input(menu)

    if opcao_do_menu == "1":
        valor = float(input("\nInforme o valor do saque: "))

        if valor > saldo:
            print("\nSaldo insuficiente.")
        elif valor > limite:
            print("\nErro! O valor do saque excede o limite.")
        elif numero_de_saques >= LIMITE_DE_SAQUES:
            print("\nErro! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}"
            numero_de_saques += 1
        else:
            print("\nErro! O valor informado é inválido.")
            
    elif opcao_do_menu == "2":
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"
        else:
            print("\nErro! Valor informado é inválido.")
            
    elif opcao_do_menu == "3":
        print("\n================ EXTRATO BANCARIO================")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=================================================")

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")