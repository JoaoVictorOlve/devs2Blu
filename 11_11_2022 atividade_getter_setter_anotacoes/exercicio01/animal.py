class Animal:
    def __init__(self, especie, raca, porte, cor):
        self.__especie = especie
        self.__raca = raca
        self.__porte = porte
        self.__cor = cor
    
    #Espécie
    @property
    def especie(self):
        return self.__especie
    @especie.setter
    def especie(self, especie):
        self.__especie = especie

    #Raça
    @property
    def raca(self):
        return self.__raca
    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    #Porte
    @property
    def porte(self):
        return self.__porte
    @raca.setter
    def porte(self, porte):
        self.__porte = porte

    #Cor
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def __str__(self):
        return f'Especie: {self.__especie}\nRaça: {self.__raca}\nPorte: {self.__porte}\nCor: {self.__cor}'