from controller import fazerCheckin, relatorioHospedes, procurarHospedes, fazerCheckout
import os


def menu():
    while True: #Loop do Menu
        os.system('cls')
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
                clienteFind = input('Digite o nome desejado\n>')
                procurarHospedes(clienteFind)
                sair = input('Pressione enter para continuar')

            case '4':
                os.system('cls')
                hospede = input('Digite o índice\n>')
                try: #Caso não dê erro, é porque foi digitado um valor que pode ser um inteiro (tipo 10)
                    intHospede = int(hospede)
                    fazerCheckout(intHospede)
                except: #Caso dê erro, é porque foi digitado um valor que não pode ser inteiro (tipo "Anderson" ou 20.492)
                    print('Valor inválido!')
                sair = input('Pressione enter para continuar')
                
            case '5':
                os.system('cls')
                print('Encerrando sistema!')
                break #Quebra o loop do menu

            case _:
                print('Valor incorreto!') #Quando é digitado qualquer outro valor, dá erro e retorna para o começo do loop do menu
                sair = input('Pressione enter para voltar')

menu()