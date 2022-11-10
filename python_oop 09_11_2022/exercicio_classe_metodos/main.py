from conta import Conta

poli = '*'*20

print(f'{poli}\nConta\n{poli}')


conta1 = Conta(str(input('Digite o nome: ')), int(input('Digite o número da conta: ')), int(input('Digite o saldo: ')), int(input('Digite o limite: ')))


conta1.depositar(int(input('Digite o valor a ser depositado: ')))
conta1.sacar(int(input('Digite o valor a ser depositado: ')))

conta2 = Conta(str(input('Digite o nome: ')), int(input('Digite o número da conta: ')), int(input('Digite o saldo: ')), int(input('Digite o limite: ')))

conta1.fazerExtrato()
print(poli)
conta2.fazerExtrato()


conta1.transferir(int(input(f'Digite o input do valor a ser extrair de {conta1.titular} para {conta2.titular}')), conta1, conta2)

conta1.fazerExtrato()
print(poli)
conta2.fazerExtrato()
