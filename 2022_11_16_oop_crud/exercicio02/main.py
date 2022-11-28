from conta import Conta
from controller import create, read, update, delete
def menu():

    
    conta = Conta()
    conta.titular = 'Jean'
    conta.numero = '123'
    conta.saldo = 20.00

    create(conta)

    lista_conta = read()

    for conta in lista_conta:
        print(conta)

    delete('123')

    read()

menu()