from conta import Conta

conta1 = Conta(str(input('Digite o titular:\n>')), int(input('Digite o número:\n>')), float(input('Digite o saldo:\n>')), float(input('Digite o limite:\n>')))
print('*'*10)
print(f'Titular: {conta1.get_titular()}\nNúmero da conta: {conta1.get_numero()}\nSaldo: {conta1.get_saldo()}')
print('*'*10)
conta2 = Conta(str(input('Digite o titular:\n>')), int(input('Digite o número:\n>')), float(input('Digite o saldo:\n>')), float(input('Digite o limite:\n>')))
print('*'*10)
print(f'Titular: {conta2.get_titular()}\nNúmero da conta: {conta2.get_numero()}\nSaldo: {conta2.get_saldo()}')
