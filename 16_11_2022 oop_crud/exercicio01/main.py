from conta import Conta
from controller import create, read
def menu():
    conta = Conta()
    conta.titular = 'Jean'
    conta.numero = '123'
    conta.saldo = 20.00

    create(conta)

    lista_contas = read()
    
    print(lista_contas)

    for c in lista_contas:
        print(c)

menu()