from pessoa import Pessoa

pessoa1 = Pessoa(str(input('Digite seu nome: ')), str(input('Digite seu CPF: ')), int(input('Digite sua idade: ')), float(input('Digite sua altura: ')))
print('*'*10)
print(f'Nome: {pessoa1.get_nome()}\nCPF: {pessoa1.get_cpf()}\nIdade: {pessoa1.get_idade()}\nAltura: {pessoa1.get_altura()}')
print('*'*10)
pessoa2 = Pessoa(str(input('Digite seu nome: ')), str(input('Digite seu CPF: ')), int(input('Digite sua idade: ')), float(input('Digite sua altura: ')))
print('*'*10)
print(f'Nome: {pessoa2.get_nome()}\nCPF: {pessoa2.get_cpf()}\nIdade: {pessoa2.get_idade()}\nAltura: {pessoa2.get_altura()}')
