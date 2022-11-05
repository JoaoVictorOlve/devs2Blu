from pessoa import Pessoa

pessoa1 = Pessoa('João Victor', 'de Oliveira', 17, '140.442.439-40')

pessoa2 = Pessoa('Marcio Lorenz', 'Alberto de Oliveira', 27, '440.557.819-04')

pessoa3 = Pessoa('Cleiton', 'Marciano', 34, '787.912.549-04')

print(pessoa1)
print(f'{pessoa1.nome} - {pessoa1.sobrenome} - {pessoa1.idade} - {pessoa1.cpf}')
print(f'{pessoa2.nome} - {pessoa2.sobrenome} - {pessoa2.idade} - {pessoa2.cpf}')
print(f'{pessoa3.nome} - {pessoa3.sobrenome} - {pessoa3.idade} - {pessoa3.cpf}')