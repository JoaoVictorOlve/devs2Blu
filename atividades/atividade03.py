
def cpf():
    lista = []
    while True:
        mulheres = 0
        acimaMedia = 0
        cpf = {}
        cpf['nome'] = str(input('Digite seu nome: '))
        while True:
            sexo = str(input('Você é homem ou mulher?: '))
            if sexo == 'homem' or sexo == 'mulher':
                cpf['sexo'] = sexo
                break
            else:
                back = input('Código inválido\nPressione enter para continuar')
            
        cpf['idade'] = int(input('Digite sua idade: '))
        lista.append(cpf)
        
        soma = 0
        for x in range(0, int(len(lista))):
            lista_cpfs = lista[x]['idade']
            soma += lista_cpfs

        media = soma / len(lista)


        print(soma)
        print(len(lista))
        #media = (soma / int(len(lista)))

        print('Pessoas cadastradas: ', len(lista))
        print('Média idade: ', str(media))
        print('Mulheres:')
        for x in range(0, int(len(lista))):
            lista_pessoas= lista[x]['sexo']
            if lista_pessoas == 'mulher':
                print('-', lista[x]['nome'])
        
        print('Pessoas com idade acima da média: ')
        for x in range(0, int(len(lista))):
            lista_idade = lista[x]['idade']
            if lista_idade > media:
                print('-', lista[x]['nome'])


cpf()