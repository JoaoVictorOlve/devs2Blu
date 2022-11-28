from carro import Carro

carro1 = Carro(input('Digite a marca: '), input('Digite o modelo: '), input('Digite a cor: '), input('Digite a categoria: '))
print('*'*10)
print(f'Marca: {carro1.get_marca()}\nModelo: {carro1.get_modelo()}\nCor: {carro1.get_cor()}\nCategoria: {carro1.get_categoria()}')
print('*'*10)
carro2 = Carro(input('Digite a marca: '), input('Digite o modelo: '), input('Digite a cor: '), input('Digite a categoria: '))
print('*'*10)
print(f'Marca: {carro2.get_marca()}\nModelo: {carro2.get_modelo()}\nCategoria: {carro2.get_categoria()}')