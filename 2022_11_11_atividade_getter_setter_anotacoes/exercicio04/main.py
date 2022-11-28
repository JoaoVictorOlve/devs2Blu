from pessoa import Pessoa

pessoa1 = Pessoa(input('Digite o nome: '), input('Digite o CPF: '), input('Digite a idade: '), input('Digite a altura: '))
print('*'*10)
print(f'{pessoa1.nome} - {pessoa1.cpf} - {pessoa1.idade} - {pessoa1.altura}')
print('*'*10)
pessoa2 = Pessoa(input('Digite o nome: '), input('Digite o CPF: '), input('Digite a idade: '), input('Digite a altura: '))
print('*'*10)
print(f'{pessoa2.nome} - {pessoa2.cpf} - {pessoa2.idade}')
print('*'*10)
