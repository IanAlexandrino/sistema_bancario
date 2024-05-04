extract = '''
EXTRACT
'''
withdraw_amount = 3
balance = 0.00

def withdraw_method(*, balance, withdraw_amount, extract):
    if(balance > 0):
        if(withdraw_amount > 0):
            print(f"\nVocê ainda tem {withdraw_amount} saques disponíveis hoje!")
            while True:
                withdraw = float(input("\nInforme o valor que vai ser retirado(saque máximo de R$ 500,00): "))
                if(withdraw > 500.0):
                    print("\nValor informado é maior que o saque máximo permitido, informe outro valor!")

                elif(withdraw < 0):
                    print("\nValor informado é menor que 0, operação inválida!")

                else:
                    print(f"\nValor de R$ {withdraw:.2f} retirado com sucesso!")
                    balance -= withdraw
                    extract += f"\nSaque: R$ {withdraw:.2f}"
                    withdraw_amount -= 1
                    break


        else:
            print("\nSua quantidade de saques diários acabou, volte amanhã ou realize outra operação!")

    else:
        print("\nUsuário não tem saldo em conta, realize um depósito antes de sacar qualquer valor!")

    return balance, withdraw_amount, extract

def deposit_method(balance, extract):
    while True:
            deposit = float(input("\nInforme o valor que vai ser depositado: "))
            if(deposit > 0):
                balance += deposit
                print(f"\nValor de R$ {deposit:.2f} inserido com sucesso na sua conta!")
                extract += f"\nDepósito: R$ {deposit:.2f}"
                break

            else: 
                print("\nValor informado para depósito inválido, insira um valor válido!")


    return balance, extract

def extract_method(balance, /, extract):
    if(len(extract) == 9):
        print("\nNão foram realizadas movimentações!")

    else:
        print(extract)
        print(f"\nSaldo atual: R$ {balance:.2f}")


while True:
    print(
        '''
        ############MENU############
        #                          #
        #        1. Saque          #
        #        2. Depósito       #
        #        3. Extrato        #
        #        0. Sair           #
        #                          #
        ############################
        '''
    )

    menu_option = int(input("Escolha a operação: "))

    if(menu_option == 1):
        result_withdraw = withdraw_method(balance = balance, withdraw_amount = withdraw_amount, extract = extract)
        balance = result_withdraw[0]
        withdraw_amount = result_withdraw[1]
        extract = result_withdraw[2]

    elif(menu_option == 2):
        result_deposit = deposit_method(balance, extract)
        balance = result_deposit[0]
        extract = result_deposit[1]

    elif(menu_option == 3):
        extract_method(balance, extract = extract)

    elif(menu_option == 0):
        print("Até a próxima!!!")
        break

    else:
        print("Opção não existe!")