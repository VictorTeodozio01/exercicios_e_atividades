def main():
    # Inicializa uma lista vazia para armazenar os equipamentos
    equipamentos = []

    # Loop para solicitar ao usuário inserir até três equipamentos
    for i in range(3):
        equipamento = input("".format(i + 1))
        equipamentos.append(equipamento)

    # Exibe a lista de equipamentos
    print("\nLista de Equipamentos:")
    for equipamento in equipamentos:
        print("- " + equipamento)

if __name__ == "__main__":
    main()