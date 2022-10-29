import os


def fazerCheckin(cliente):
    with open('hotel.txt', 'a') as arquivo: #Abre o arquivo para vinculação
        arquivo.write(str(cliente)+"\n") #Adiciona hóspede no arquibo
        arquivo.close() #Fecha o arquivo

        
def relatorioHospedes():
    os.system('cls')
    lista = [] #Lista onde ficará os hóspedes

    with open('hotel.txt', 'r') as arquivo: #Abre o arquivo para ler
        for numero, linha in enumerate(arquivo): #Lê o arquivo linha por linha
            hospede = eval(linha) #Converte a linha do arquivo em um dicionário

            hospede['id'] = str(numero)
            #Cria uma chave id, que vai receber como valor a posição da sua linha
            #Ex: Hóspede está na linha 0, logo id é 0

            lista.append(hospede) #Vincula o dicionário do hóspede à lista
    arquivo.close() #Fecha o arquivo

    #Imprimindo a tabela dos hóspedes na tela
    print('='*70)
    print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(' Id', ' Nome', ' Sobrenome', ' Idade')) #Cabeçalho
    print('='*70)
    for index in range(0, len(lista)): #Lista os hóspedes índice por índice
        print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(lista[index]['id'],lista[index]['nome'],lista[index]['sobrenome'],lista[index]['idade'])) #Imprime todos os hóspedes na tela
        print('='*70)





def procurarHospedes(clienteFind):
    os.system('cls')
    lista = [] #Lista onde ficará os hóspedes
    listaEncontrados = [] #Lista dos hóspedes encontrados 
    encontrado = False

    with open('hotel.txt', 'r') as arquivo: #Abre o arquivo para ler
        for numero, linha in enumerate(arquivo): #Lê o arquivo linha por linha
            hospede = eval(linha) #Converte a linha do arquivo em um dicionário
            hospede['id'] = str(numero) #Cria o id do hóspede de acordo com sua posição no arquivo
            lista.append(hospede) #Vincula o hóspede à lista
    arquivo.close() #Fecha o arquivo

    for index in range(0, len(lista)): #Lê a lista índice por índice
        if clienteFind == lista[index]['nome']: #Se o nome digitado for o mesmo do hospede do indice
            encontrado = True
            listaEncontrados.append(lista[index]) #Coloca esse hóspede encontrado na lista de encontrados
    if encontrado == True: #Se o nome de um ou mais hóspedes foram encontrados
        #Tabela dos hóspedes encontrados
        print('='*70)
        print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(' Id', ' Nome', ' Sobrenome', ' Idade')) #Cabeçalho
        print('='*70)
        for index in range(0, len(listaEncontrados)): #Lista os hóspedes encontrados índice por índice
            print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(listaEncontrados[index]['id'],listaEncontrados[index]['nome'],listaEncontrados[index]['sobrenome'],listaEncontrados[index]['idade'])) #Imprime todos os hóspedes na tela
            print('='*70)

        sair = input('Pressione enter para continuar')
    else:
        sair = input('Hóspede não encontrado!\nPressione enter para continuar')


def fazerCheckout(clienteFind):
    os.system('cls')
    lista = [] #Lista onde ficará os hóspedes
    encontrado = False

    with open('hotel.txt', 'r') as arquivo: #Abre o arquivo para ler
        for numero, linha in enumerate(arquivo): #Lê o arquivo linha por linha
            hospede = eval(linha) #Converte a linha do arquivo em um dicionário
            hospede['id'] = str(numero) #Cria o id do hóspede acordo com sua posição no arquivo
            lista.append(hospede) #Vincula o dicionário do hóspede à lista

    for index in range(0, len(lista)): #Lê a lista índice por índice
        if clienteFind == lista[index]['id']: # Se o indice for encontrado
            encontrado = True

            #Tabela do hóspede encontrado
            os.system('cls')
            print('='*70)
            print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(' Id', ' Nome', ' Sobrenome', ' Idade')) #Cabeçalho
            print('='*70)
            print('|{:^5}|{:^20}|{:^20}|{:^20}'.format(lista[index]['id'],lista[index]['nome'],lista[index]['sobrenome'],lista[index]['idade'])) #Imprime todos os hóspedes na tela
            print('='*70) #Cita apenas um hóspede, logo não preciso de um loop
            while True: 
                apagar = input('Deseja apagar?(S/N)\n>')
                if apagar == 'S': #Se quiser apagar
                    del lista[index] #Deleta esse hóspede da lista
                    with open('hotel.txt', 'w') as arquivo: #Abre o arquivo para escrever
                        for index in range(0, len(lista)): #Lê a lista linha por linha
                            del lista[index]['id'] #Deleta a chave id antes de entrar no arquivo para não gerar conflito
                            arquivo.write(str(lista[index])+'\n') #Joga novamente a lista de hóspedes para o arquivo
                    arquivo.close() #Fecha o arquivo
                    break #Quebra o loop do while e volta para o menu
                elif apagar == 'N': #Se não quiser apagar
                    break #Apenas quebra o loop do while e volta para o menu
                else: #Se for digitado qualquer outro valor
                    sair = input('Valor incorreto!\nPressione enter para continuar')
                    os.system('cls') #Avisa e volta para o começo do loop
            break #Para quebrar o loop do for (evita o erro "index out of range")
    
    if encontrado == False: #Se o hóspede não foi encontrado
        os.system('cls')
        sair = input('Cliente não encontrado\nPressione enter para continuar')