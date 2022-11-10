class Carro:
    marca = ''
    modelo = ''
    valor = 0

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nValor: {self.valor}'