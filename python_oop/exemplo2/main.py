from conta import Conta

conta = Conta()

conta.titular = 'Lira'
conta.numero = 123456
conta.saldo = 120
conta.limite = 1200.00

conta1 = Conta()

conta1.titular = 'Haiko'
conta1.numero = 98654
conta1.saldo = 130
conta1.limite = 1300.00

conta2 = Conta()
conta2.titular = 'Jean'
conta2.numero = 4984234
conta2.saldo = 150
conta2.limite = 1500.00

print(conta)
print(conta1)
print(conta2)