from controller import fazerCheckin, relatorioHospedes, procurarHospedes, fazerCheckout
import os
import uuid

def menu():
    while True:
        poli = '='*10
        print(f'{poli}\n1 - Fazer Check in\n2 - Relatório Hóspedes\n3 - Procurar Hóspedes\n4 - Fazer Check out\n5 - Finalizar Atendimento\n{poli}')
        
        pedido = input(':>')
        match pedido:
            case '1': #Check-in
                cliente = {}
                cliente['nome'] = str(input('Digite seu nome: '))
                cliente['sobrenome'] = str(input('Digite seu sobrenome: '))
                cliente['idade'] = str(input('Digite sua idade: '))
                fazerCheckin(cliente)
            case '2':
                file_size = os.path.getsize('hotel.txt')
                if file_size == 0:
                    print('Lista está vazia')
                else:
                    relatorioHospedes()
            case '3':
                clienteFind = str(input('Digite o nome desejado:'))
                procurarHospedes(clienteFind)
            case '4':
                clienteFind = str(input('Digite o nome: '))
                fazerCheckout(clienteFind)
            case _:
                print('Valor incorreto!')
                sair = input('Pressione enter para voltar')
menu()