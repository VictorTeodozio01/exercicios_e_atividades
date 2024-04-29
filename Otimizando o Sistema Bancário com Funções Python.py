import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1] Sacar
    [2] Depositar
    [3] Visualizar Extrato
    [4] Criar Conta Corrente
    [5] Listar contas
    [6] Criar Usuario
    
    Selecione uma opção:
    
     """
    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_de_saques):

    if valor > saldo:
        print("\nSaldo insuficiente.")
    elif valor > limite:
        print("\nErro! O valor do saque excede o limite.")
    elif numero_de_saques >= limite_de_saques:
        print("\nErro! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_de_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nErro! O valor informado é inválido.")

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nErro! O valor informado é inválido.")

    return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO BANCARIO================")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n=================================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe nome completo: ")
    data_de_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data de nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_da_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero da conta": numero_da_conta, "usuario": usuario}
    print("\nUsuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero da conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numero_de_saques,
                LIMITE_DE_SAQUES=LIMITE_DE_SAQUES,
            )
        elif opcao == "2":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "3":
            visualizar_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            numero_da_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_da_conta, usuarios)
            
            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)
            
        elif opcao == "6":
            criar_usuario(usuarios)

        else:
            print("\nOperação inválida")

main()