import os

def fazerCheckin(cliente):
    with open('hotel.txt', 'a') as arquivo: #Abre o arquivo para vinculação
        arquivo.write(str(cliente)+"\n") #Adiciona hóspede no arquivo
        arquivo.close() #Fecha o arquivo

def relatorioHospedes():
    os.system('cls')

    print('='*70)
    print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(' Id', ' Nome', ' Sobrenome', ' Idade')) #Cabeçalho
    print('='*70)

    with open('hotel.txt', 'r') as arquivo: #Abre o arquivo para ler
        for numero, linha in enumerate(arquivo): #Lê o arquivo linha por linha
            hospede = eval(linha) #Converte a linha do hóspede em dicionário
            hospede['id'] = str(numero)
            #Cria uma chave id, que vai receber como valor a posição da sua linha
            #Ex: Hóspede está na linha 0, logo id é 0
            print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(hospede['id'],hospede['nome'],hospede['sobrenome'],hospede['idade'])) 
            print('='*70) #Cita esse hóspede na tabela

    arquivo.close() #Fecha o arquivo

def procurarHospedes(clienteFind):
    os.system('cls')
    listaEncontrados = [] #Lista dos hóspedes encontrados 
    encontrado = False

    with open('hotel.txt', 'r') as arquivo: #Abre o arquivo para ler
        for numero, linha in enumerate(arquivo): #Lê o arquivo linha por linha
            hospede = eval(linha) #Converte a linha do hóspede em um dicionário

            if clienteFind == hospede['nome']: #Se for encontrado o hóspede
                encontrado = True
                hospede['id'] = str(numero) #Cria o id do hóspede de acordo com sua posição no arquivo
                listaEncontrados.append(hospede) #Vincula o hóspede à lista dos encontrados

    arquivo.close() #Fecha o arquivo

    if encontrado == True: #Se o nome de um ou mais hóspedes foram encontrados
        #Tabela dos hóspedes encontrados
        print('='*70)
        print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(' Id', ' Nome', ' Sobrenome', ' Idade')) #Cabeçalho
        print('='*70)
        for index in range(0, len(listaEncontrados)): #Lista os hóspedes encontrados índice por índice
            print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(listaEncontrados[index]['id'],listaEncontrados[index]['nome'],listaEncontrados[index]['sobrenome'],listaEncontrados[index]['idade'])) #Imprime todos os hóspedes na tela
            print('='*70) #Cita esse hóspede na tabela

    else: #Se nenhum hóspede foi encontrado
        print('Hóspede não encontrado!')

def fazerCheckout(hospede):
    os.system('cls')

    with open('hotel.txt') as arquivo: #Abre o arquivo para ler
        lines = arquivo.readlines() #Lê todas as linhas
    arquivo.close()
    
    if hospede <= len(lines) - 1: #Se o valor não for maior que as linhas do arquivo (ou seja, realmente tem um indice ali)
        hospedeEncontrado = eval(lines[hospede]) #Converte a linha do hóspede para dicionário

        print('='*70)
        print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(' Id', ' Nome', ' Sobrenome', ' Idade')) #Cabeçalho
        print('='*70)
        print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(hospede,hospedeEncontrado['nome'],hospedeEncontrado['sobrenome'],hospedeEncontrado['idade'])) #Imprime todos os hóspedes na tela
        print('='*70) #Informa qual foi o hóspede apagado

        del lines[hospede] #Apaga o hóspede dentro da lista

        with open('hotel.txt', 'w') as arquivo: #Apaga tudo dentro do arquivo e insere a nova lista sem o hóspede apagado
            for line in lines: #Lê a lista índice por índice
                arquivo.write(line) #Escreve cada hóspede dentro da lista para o arquivo
        arquivo.close()

        print('Hóspede apagado!')

    else: #Se o hóspede não foi encontrado
        print('Hóspede não encontrado!')