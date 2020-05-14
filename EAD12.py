'''
    Hotel Bom Descanso - Software para reserva de quartos
'''

quartos = {}

contiua_cadastro = "SIM"

print('''
            Software para reserva de quartos
            [1] - Nova Reserva
            [2] - Remover Reserva
            [3] - Exibir Relatório
            [4] - Sair do Programa
        ''')

opcao = int(input('Digite a opção: '))

while opcao!= 4:
        # [1] - Nova Reserva
        if opcao == 1:
            quarto = input('Informe o número do quarto: ')
            hospede = input('Informe o nome do hóspede: ')

            if quarto in quartos:
                print('JÁ EXISTE ESSE QUARTO CADASTRADO, ESCOLHA OUTRO')
                continue
            else:
                print('RESERVANDO QUARTO...')
                quartos[quarto] = hospede.upper()
                contiua_cadastro = input('Deseja cadastrar mais um quarto? (Sim ou Não) \n')
                if contiua_cadastro.upper() == "SIM":
                    opcao == 1
                else:
                    contiua_cadastro == "SIM"
                    opcao = int(input('Digite a opção: '))
        # [2] - Remover Reserva
        elif opcao == 2:
            print('REMOVER RESERVA')
            quarto = input('Informe o número do quarto: ')
            if quarto in quartos:
                del quartos[quarto]
                print('DELETANDO RESERVA...')
                continua = input('Deseja excluir mais uma reserva? (Sim ou Não)')
                if continua.upper() == "SIM":
                    if quarto in quartos:
                        del quartos[quarto]
                        print('DELETANDO RESERVA...')
                else:
                    opcao = int(input('Digite a opção: '))

        # [3] - Exibir Relatório
        elif opcao == 3:
            # Relatórios dos quartos reservados
            print('\n')
            print("RELATÓRIOS DOS QUARTOS RESERVADOS")
            for key, value in quartos.items():
                print(f'QUARTO Nº {key} = {value}')

            print("\nFIM DO RELATÓRIO")
            opcao = int(input('Digite a opção: \n'))
        # [4] - Sair do Programa
        else:
            print("SAINDO DO PROGRAMA...")
            break
else:
    print('\n')

