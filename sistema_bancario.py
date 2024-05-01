extract = '''
EXTRACT
'''
withdraw_amount = 3
balance = 500.00

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


    elif(menu_option == 2):
        print(2)

    elif(menu_option == 3):
        print(3)

    elif(menu_option == 0):
        print("Até a próxima!!!")
        break

    else:
        print("Opção não existe!")