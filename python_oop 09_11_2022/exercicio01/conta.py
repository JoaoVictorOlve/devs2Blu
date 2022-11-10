class Conta:
    numero = 0
    titular = ''
    saldo = 0
    limite = 0

    def __str__(self):
        return f'Número: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}\nLimite: {self.limite}'