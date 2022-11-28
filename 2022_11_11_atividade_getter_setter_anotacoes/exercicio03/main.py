from conta import Conta

conta1 = Conta(input('Digite o titular: '), input('Digite o número: '), input('Digite o saldo: '), input('Digite o limite: '))
print('*'*10)
print(f'Titular: {conta1.titular}\nNúmero: {conta1.numero}\nSaldo: {conta1.saldo}\nLimite: {conta1.limite}')
print('*'*10)
conta2 = Conta(input('Digite o titular: '), input('Digite o número: '), input('Digite o saldo: '), input('Digite o limite: '))
print(f'Titular: {conta2.titular}\nNúmero: {conta2.numero}\nSaldo: {conta2.saldo}')
