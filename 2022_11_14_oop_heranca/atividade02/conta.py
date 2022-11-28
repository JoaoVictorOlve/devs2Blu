class Conta:
    def __init__(self, numero, agencia, tipo):
        self.__numero = numero
        self.__agencia = agencia
        self.__tipo = tipo
        print('Passando pelo construtor da classe Conta')
    
    def __str__(self):
        return f'{self.__numero} - {self.__agencia} - {self.__tipo}'