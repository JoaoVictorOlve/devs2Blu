from model.pessoaJuridica import PessoaJuridica

def create_pj(conta):
    contas = open('avaliacao/banco/pessoajuridica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close()

def read_pj():
    lista_contas = []
    contas = open('avaliacao/banco/pessoajuridica.txt', 'r')
    
    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        print(conta_objeto)

        pessoaJuridica = PessoaJuridica()
        pessoaJuridica.agencia = conta_objeto[0]
        pessoaJuridica.numero_agencia = conta_objeto[1]

        pessoaJuridica.titular = conta_objeto[2]
        pessoaJuridica.cnpj = conta_objeto[3]
        pessoaJuridica.saldo_inicial = conta_objeto[4]
        pessoaJuridica.segundo_titular = conta_objeto[5]

        lista_contas.append(pessoaJuridica)
    contas.close()

    