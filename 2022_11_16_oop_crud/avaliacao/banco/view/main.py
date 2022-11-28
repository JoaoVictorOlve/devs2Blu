from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

def menu():
    menu = 1

    while(menu != 0):
        print('Digite a opção desejada!')

        menu_inicial = int(input('1 - Pessoa Física\n2 - Pessoa Jurídica\n>'))

        match menu_inicial:

            case 1:
                #Pessoa Física
                menu = int(input('1 - Criar Conta de Pessoa Física\n2 - Listar Contas\n>'))

                match menu:
                    case 1:
                        pessoaFisica = PessoaFisica()
                        pessoaFisica.titular = input('Titular: ')
                        pessoaFisica.cpf = input('CPF: ')
                        pessoaFisica.saldo_inicial = input('Saldo inicial: ')
                        while True:
                            cad_segundo_titular = input('Deseja cadastrar um segundo titular?(S/N): ')
                            if cad_segundo_titular == 'S':
                                seg_titular = input('Segundo titular: ')
                                pessoaFisica.segundo_titular = seg_titular
                                break
                            elif cad_segundo_titular == 'N':
                                break
                            else:
                                print('Valor inválido!')
                        create_psf(pessoaFisica)
                    case 2:
                        read_psf()
            case 2:
                menu = int(input('1 - Criar Conta de Pessoa Jurídica\n2 - Listar Contas'))
                match menu:
                    case 1:
                        pessoaJuridica = PessoaJuridica()
                        pessoaJuridica.titular = input('Titular: ')
                        pessoaJuridica.cnpj = input('CNPJ: ')
                        pessoaJuridica.saldo_inicial = input('Saldo inicial: ')
                        while True:
                            cad_segundo_titular = input('Deseja cadastrar um segundo titular?(S/N): ')
                            if cad_segundo_titular == 'S':
                                seg_titular = input('Segundo titular: ')
                                pessoaJuridica.segundo_titular = seg_titular
                                break
                            elif cad_segundo_titular == 'N':
                                break
                            else:
                                print('Valor inválido!')
                        create_pj(pessoaJuridica)
                    case 2:
                        read_pj()
                #Pessoa Jurídica