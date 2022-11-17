from model import Conta

def create(conta):
    #Variavel referencia para TXT
    contas = open('contas.txt', 'a')
    #Variavel de Referencia de escrita
    contas.write(str(conta)+'\n')
    #Variavel de referencia fechando nosso arquivo
    contas.close
    

def read():
    #Lista Vazia
    lista_contas = []
    #Variavel referencia arquivo txt
    contas = open('contas.txt', 'r')
    #for com variavel percorrendo arquivo txt
    for conta in contas:
        #variavel conta recebendo função internalizada para retirada espaços
        conta = conta.strip()
        #variavel recebendo função internalizada de condição para o indice
        conta__objeto = conta.split(';')

        print(conta__objeto)
        #Variavel referencia objeto
        conta = Conta()
        #Setter recebendo um indice
        conta.titular = conta__objeto[0]
        #Setter recebendo um indice
        conta.numero = conta__objeto[1]
        #Setter recebendo um indice
        conta.saldo = conta__objeto[2]

        lista_contas.append(conta)
    
    contas.close
    return lista_contas