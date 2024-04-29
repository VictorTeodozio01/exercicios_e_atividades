import textwrap

class Usuario:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Conta:
    LIMITE_DE_SAQUES = 3

    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_de_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nErro! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\nSaldo insuficiente.")
        elif valor > 500:  # supondo limite fixo de saque em 500
            print("\nErro! O valor do saque excede o limite.")
        elif self.numero_de_saques >= Conta.LIMITE_DE_SAQUES:
            print("\nErro! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_de_saques += 1
            print("\nSaque realizado com sucesso!")
        else:
            print("\nErro! O valor informado é inválido.")

    def visualizar_extrato(self):
        print("\n================ EXTRATO BANCARIO================")
        print("\nNão foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("\n=================================================")

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print("\nJá existe usuário com esse CPF!")
            return

        nome = input("Informe nome completo: ")
        data_nascimento = input("Informe a data de nascimento: ")
        endereco = input("Informe o endereço: ")

        novo_usuario = Usuario(cpf, nome, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)
        print("\nUsuário criado com sucesso!")

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta_corrente(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_da_conta = len(self.contas) + 1
            nova_conta = Conta(self.agencia, numero_da_conta, usuario)
            self.contas.append(nova_conta)
            print("\nConta criada com sucesso!")
            return nova_conta
        print("\nUsuário não encontrado!")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero}
                Titular:\t{conta.usuario.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

def menu():
    menu_text = """\n
    ================ MENU ================
    [1] Sacar
    [2] Depositar
    [3] Visualizar Extrato
    [4] Criar Conta Corrente
    [5] Listar contas
    [6] Criar Usuario
    
    Selecione uma opção:
    
     """
    return input(textwrap.dedent(menu_text))

def main():
    banco = Banco()
    while True:
        opcao = menu()

        if opcao == "1":
            if not banco.contas:
                print("\nNenhuma conta disponível para saque.")
                continue
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero == numero_conta), None)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            else:
                print("\nConta não encontrada.")
        elif opcao == "2":
            if not banco.contas:
                print("\nNenhuma conta disponível para depósito.")
                continue
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero == numero_conta), None)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("\nConta não encontrada.")
        elif opcao == "3":
            if not banco.contas:
                print("\nNenhuma conta disponível para visualizar o extrato.")
                continue
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((c for c in banco.contas if c.numero == numero_conta), None)
            if conta:
                conta.visualizar_extrato()
            else:
                print("\nConta não encontrada.")
        elif opcao == "4":
            banco.criar_conta_corrente()
        elif opcao == "5":
            banco.listar_contas()
        elif opcao == "6":
            banco.criar_usuario()
        else:
            print("\nOperação inválida")

if __name__ == "__main__":
    main()
