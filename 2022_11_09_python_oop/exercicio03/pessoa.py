class Pessoa:
    nome = ''
    cpf = ''
    idade = 0

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}'