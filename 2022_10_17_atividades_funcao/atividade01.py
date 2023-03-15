
def lerFuncionario():
    funcionario = {}
    funcionario['nome'] = str(input('Digite seu nome: '))
    funcionario['nascimento'] = str(input('Digite sua data de nascimento: '))
    funcionario['carteira_trabalho'] = int(input('Digite sua carteira de trabalho: '))

    if funcionario['carteira_trabalho'] != 0:
        funcionario['primeiro_ano_contratacao'] = str(input('Informe seu primeiro ano de contratação: '))
        funcionario['salario'] = float(input('Informe seu salario: '))

    print('Nome:', funcionario['nome'])
    print('Nascimento:', funcionario['nascimento'])
    print('Carteira de Trabalho:', funcionario['carteira_trabalho'])
    if funcionario['carteira_trabalho'] != 0:
        print('Primerio Ano Contratação:', funcionario['primeiro_ano_contratacao'])
        print('Salário:', funcionario['salario'])

lerFuncionario()

#teste