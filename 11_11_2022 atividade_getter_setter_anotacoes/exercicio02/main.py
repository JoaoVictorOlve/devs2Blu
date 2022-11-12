from carro import Carro

carro1 = Carro(input('Digite a marca:'), input('Digite o modelo: '), input('Digite a cor: '), input('Digite a categoria: '))

print(f'{carro1.marca} - {carro1.modelo} - {carro1.cor} - {carro1.categoria}')

carro2 = Carro(input('Digite a marca:'), input('Digite o modelo: '), input('Digite a cor: '), input('Digite a categoria: '))

print(f'{carro2.marca} - {carro2.modelo} - {carro2.categoria}')