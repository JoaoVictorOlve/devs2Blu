from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

poli = '*'*10

while True:
    print(f'{poli}\nConta de Banco\n{poli}\nQual seu tipo de conta?\n1 -> Física\n2 -> Juridica')
    resultado = input('>')
    
    match resultado:

        case '1':
            titular = input('Insira seu nome: ')
            cpf = input('Insira seu CPF: ')
            saldo_inicial = float(input('Insira seu saldo: '))
            pessoaFisica1 = PessoaFisica(titular, cpf, saldo_inicial)
            while True:
                cad_titular = input('Deseja cadastrar novo titular? (S/N)')
                if cad_titular == 'S':
                    segundo_titular = input('Insira o segundo titular\n>')
                    pessoaFisica1.segundo_titular = segundo_titular
                    break
                elif cad_titular == 'N':
                    break
                else:
                    print('Valor inválido!')

            print(pessoaFisica1)
        case '2':
            titular = input('Insira seu nome: ')
            cnpj = input('Insira seu CPF: ')
            saldo_inicial = float(input('Insira seu saldo: '))
            pessoaJuridica1 = PessoaJuridica(titular, cnpj, saldo_inicial)
            while True:
                cad_titular = input('Deseja cadastrar novo titular? (S/N)\n>')
                if cad_titular == 'S':
                    segundo_titular = input('Insira o segundo titular:\n>')
                    pessoaJuridica1.segundo_titular = segundo_titular
                    break
                elif cad_titular =='N':
                    break
                else:
                    print('Valor inválido!')

            print(pessoaJuridica1)    
            
        case other:
            print('Valor errado!')