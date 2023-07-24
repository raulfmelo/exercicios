import os


def menu():
    limpaTela()
    menu = """\n
    ==========MENU=========
    [u]\tNovo usuário      |
    [n]\tNova conta        |
    [l]\tListar contas     |
    [d]\tDepositar         |
    [s]\tSacar             |
    [e]\tExtrato           |
    [q]\tSair              |
    =======================
    => """
    return input(menu)


def depositar(saldo, valor, extrato):
    limpaTela()
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("===Depósito efetuado com SUCESSO!===")
    else:
        print(
            "Error:Invalid Value, valores negativos não são aceitos como depósito: 0x7217190"
        )

    return saldo, extrato


def saque(saldo, valor, extrato, numero_saques, limite):
    limpaTela()
    if valor > saldo:
        print("Error:Invalid Operation, SALDO INSUFICIENTE")
    elif valor > limite:
        print("Error:Invalid Operation, Valor do saque ultrapassa o limite.")
    else:
        numero_saques += 1
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        print("===Saque efetuado com SUCESSO!===")
    return saldo, extrato, numero_saques


def pega_extrato(extrato):
    print(extrato)


def criar_usuario(usuarios: list):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Error: Invalid Operation, usuário já cadastrado")
        input("Pressiona ENTER para continuar...")
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla do estado): "
    )

    usuarios.append(
        {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }
    )

    print("Usuário cadastrado com SUCESSO!")
    input("Pressione ENTER para continuar...")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com SUCESSO!")
        input("Pressione ENTER para continuar...")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Error:Invalid User, Usuário não encontrado.")
    input("Pressione ENTER para continuar...")


def listar_contas(contas: list):
    for conta in contas:
        linha = f"""
            Agencia:\t {conta['agencia']}
            C/C:\t {conta['numero_conta']}
            Titular:\t {conta['usuario']['nome']}
        """
        print("=======================================================")
        print(linha)


def limpaTela():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # constantes
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # variaveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # loop do programa
    while True:
        opcao = menu()

        if opcao == "d":
            limpaTela()
            valor = float(input("Digite o valor do depósito: R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)
            input("pressione ENTER para continuar...")
        elif opcao == "s":
            limpaTela()
            if numero_saques >= 3:
                print("Error:Invalid Operation, quantidades de saques diários")
            else:
                valor = float(input("Digite o valor do saque: R$ "))
                if valor >= 0:
                    saldo, extrato, numero_saques = saque(
                        saldo, valor, extrato, numero_saques, limite
                    )
                else:
                    print(
                        "Error:Invalid Operation, Apenas valores positivos são aceitos!"
                    )
            input("Pressione ENTER para continuar...")
        elif opcao == "e":
            limpaTela()
            print("\n================ EXTRATO ================")
            pega_extrato(extrato)
            print(f"Saldo : R${saldo: .2f}")
            print("==========================================")
            input("Pressione ENTER para continuar...")
        elif opcao == "n":
            limpaTela()
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "l":
            limpaTela()
            listar_contas(contas)
            print("=======================================================")
            input("Pressionae Enter para continuar...")
        elif opcao == "u":
            limpaTela()
            criar_usuario(usuarios)
        elif opcao == "q":
            limpaTela()
            print("Muito obrigado por utilizar a nossa plataforma!")
            input("Pressione ENTER para encerrar o programa...")
            break
        else:
            limpaTela()
            print("Error:Invalid Option, opção inválida!")
            input("Pressione ENTER para continuar...")


main()
