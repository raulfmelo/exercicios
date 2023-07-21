import os

menu = """
    Menu
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
"""
# VARIAVEIS E CONSTANTES
LIMITE_DIARIO = 500
LIMITE_DE_SAQUE = 3
limitador_diario = 0
limitador_de_saque = 0
saldo = 0
extrato = ""

while True:
    # IMPRIME O MENU
    os.system("cls" if os.name == "nt" else "clear")
    option = input(menu)

    # VALIDAÇÂO DE DEPOSITO
    if option == "d":
        os.system("cls" if os.name == "nt" else "clear")
        valor_deposito = float(input("Qual valor deseja depositar: R$"))
        if valor_deposito > 0:
            os.system("cls" if os.name == "nt" else "clear")
            saldo += valor_deposito
            print(f"Valor depositado: R$:{valor_deposito: .2f}")
            print(f"Seu Saldo é de R${saldo: .2f}")
            extrato += f"Deposito: R${valor_deposito: .2f}\n"
            input("Pressione ENTER para continuar...")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Apenas valores positivos podem ser depositados.")
            input("Pressione ENTER para continuar...")

    # VALIDAÇÂO DE SAQUE
    elif option == "s":
        os.system("cls" if os.name == "nt" else "clear")
        if limitador_de_saque >= LIMITE_DE_SAQUE:
            print("você já realizou 3 saques hoje, volte amanhã")
            input("Pressione ENTER para continuar...")
        else:
            saque = float(input("Qual valor deseja sacar: R$"))
            os.system("cls" if os.name == "nt" else "clear")
            if saque > saldo:
                print("Saldo Insulficiente")
                input("Pressione ENTER para continuar...")
            elif limitador_diario > LIMITE_DIARIO:
                print(
                    f"Seu limite diario de R${LIMITE_DIARIO: .2f} já foi atingido, volte amanhã"
                )
                input("Pressione ENTER para continuar...")
            elif saque + limitador_diario > LIMITE_DIARIO:
                print(
                    f"O valor do saque ultrapassa seu limite diario de R${LIMITE_DIARIO: .2f}"
                )
                input("Pressione ENTER para continuar...")
            else:
                limitador_de_saque += 1
                saldo -= saque
                limitador_diario += saque
                print(
                    f"""
Você sacou R${saque: .2f}, e seu saldo atual é de R${saldo: .2f}
Seu limite diario esta em R${limitador_diario: .2f} e ainda pode sacar R${LIMITE_DIARIO - limitador_diario: .2f}
                        """
                )
                extrato += f"Saque: R${saque: .2f}\n"
                input("Pressione ENTER para continuar...")

    # VALIDAÇÂO DO EXTRATO
    elif option == "e":
        os.system("cls" if os.name == "nt" else "clear")
        print(extrato)
        print(f"Seu saldo esta em : R${saldo: .2f}")
        input("Pressione ENTER para continuar...")
    elif option == "q":
        os.system("cls" if os.name == "nt" else "clear")
        print("Muito obrigado por utlizar o nosso sistema, até mais!")
        input("Pressione ENTER para continuar...")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("digite uma opção válida")
        input("Pressione ENTER para continuar...")
