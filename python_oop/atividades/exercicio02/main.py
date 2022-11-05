from conta import Conta

conta1 = Conta(123, 'Janaina', 240, 3500.00)

conta2 = Conta(456, 'Jeandro', 356, 2323.20)

conta3 = Conta(789, 'Juquinha', 789, 5500.20)

print(conta1)

print(f'{conta1.numero} - {conta1.titular} - {conta1.saldo} - {conta1.limite}')

print(f'{conta2.numero} - {conta2.titular} - {conta2.saldo} - {conta2.limite}')

print(f'{conta3.numero} - {conta3.titular} - {conta3.saldo} - {conta3.limite}')