class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    def fazerExtrato(self):
        print(f'Numero da Conta: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}')
    
    def depositar(self, valor):
        self.saldo += valor
        return f'Depositado o valor de R${valor} na conta!'

    def sacar(self, valor):
        self.saldo -= valor
        return f'Sacando o valor de R${valor} na conta!'

    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)
        return f'Transferido o valor de R${valor} de {origem} para {destino}'