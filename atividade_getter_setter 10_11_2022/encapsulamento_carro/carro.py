class Carro:
    def __init__(self, marca, modelo, cor, categoria):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__categoria = categoria

#   Marca
    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

#   Modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

#   Cor
    def set_cor(self, cor):
        self.__cor = cor

    def get_cor(self):
        return self.__cor

#   Categoria
    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_categoria(self):
        return self.__categoria

    def __str__(self):
        print(f'Marca: {self.get_marca()}\nModelo: {self.get_modelo()}\nCor: {self.get_cor()}\nCategoria: {self.get_categoria()}')