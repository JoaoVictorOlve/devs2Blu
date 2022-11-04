class Conta:
    def __init__(self, numero, titular, saldo, cpf, limite):
        print(f'Imprimindo variavel referencia {self}')

        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.cpf = cpf
        self.limite = limite