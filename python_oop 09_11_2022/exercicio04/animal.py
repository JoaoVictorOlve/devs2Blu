class Animal:
    especie = ''
    cor = ''
    raca = ''

    def __str__(self):
        return f'Espécie: {self.especie}\nCor: {self.cor}\n Raça: {self.raca}'