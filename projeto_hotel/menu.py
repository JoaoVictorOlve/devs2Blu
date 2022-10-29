from controller import fazerCheckin, relatorioHospedes, procurarHospedes, fazerCheckout
import os
import time



def menu():
    os.system('cls')
    while True: #Loop do Menu
        poli = '='*10 #Cabeçalho
        print(f'{poli}\n1 - Fazer Check in\n2 - Relatório Hóspedes\n3 - Procurar Hóspedes\n4 - Fazer Check out\n5 - Finalizar Atendimento\n{poli}')
        
        pedido = input(':>')
        match pedido:
            case '1': #Check-in
                os.system('cls')
                hospede = {} #Cria um dicionário do hóspede
                hospede['nome'] = str(input('Digite seu nome\n>'))
                hospede['sobrenome'] = str(input('Digite seu sobrenome\n>'))
                hospede['idade'] = str(input('Digite sua idade\n>'))
                fazerCheckin(hospede)
                sair = input('Hóspede cadastrado!\nPressione enter para continuar')

            case '2':
                os.system('cls')
                file_size = os.path.getsize('hotel.txt') #Se o arquivo não tem nenhuma memória, logo está vazio
                if file_size == 0: #Se arquivo estiver vazio
                    sair = input('Lista está vazia!\nPressione enter para continuar')

                else:
                    relatorioHospedes()
                    sair = input('Pressione enter para continuar')

            case '3':
                os.system('cls')
                clienteFind = str(input('Digite o nome desejado\n>'))
                procurarHospedes(clienteFind)

            case '4':
                os.system('cls')
                clienteFind = input('Digite o índice\n>')
                fazerCheckout(clienteFind)
            case '5':
                os.system('cls')
                print('Encerrando sistema!')
                time.sleep(3)
                break #Quebra o loop do menu

            case _:
                print('Valor incorreto!')
                sair = input('Pressione enter para voltar')

menu()