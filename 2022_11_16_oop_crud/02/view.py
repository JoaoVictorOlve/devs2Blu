from model import Conta
from controller import create, read

abacate = Conta()
abacate.titular = 'João Victor de Oliveira'
abacate.numero = '1234'
abacate.saldo = 200.00

create(abacate)

lista_abacates = read()

print(lista_abacates)

print('*'*30)

for c in lista_abacates:
    print(c)