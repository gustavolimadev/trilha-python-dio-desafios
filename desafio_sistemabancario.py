menu = """
==============================================
Selecione uma das opções: 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==============================================
=> """

saldo = 0
limite = 500
extrato = ''''''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("insira o valor do deposito | R$: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor:.2f} \n'

        else:
            print("o valor informado não é válido")



    elif opcao == "s":
        valor = float(input("insira o valor do saque | R$: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite:
            print(f"Você não pode sacar mais que R${saldo}")

        elif excedeu_saques:
            print("Você não pode mais realizar saques hoje")

        elif valor > 0: 
            saldo -= valor
            extrato += f'Saque de R$ {valor:.2f} \n' 
            numero_saques += 1

        else:
            print("O valor informado não é válido")          



    elif opcao == "e":
        print("Extrato")
        extrato += f"Saldo: R$ {saldo}"
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada")