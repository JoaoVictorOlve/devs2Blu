from animal import Animal

animal1 = Animal(input('Digite a espécie: '), input('Digite a raça: '), input('Digite o porte: '), input('Digite a cor: '))
print('*'*10)
print(f'{animal1.especie} - {animal1.raca} - {animal1.porte} - {animal1.cor}')

animal2 = Animal(input('Digite a espécie: '), input('Digite a raça: '), input('Digite o porte: '), input('Digite a cor: '))
print(f'{animal2.especie} - {animal2.raca} - {animal2.cor}')
