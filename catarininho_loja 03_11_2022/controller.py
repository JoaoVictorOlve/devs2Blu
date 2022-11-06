def cadastroProduto(produto):

    with open('produtos.txt', 'a') as arquivo:
        arquivo.write(str(produto)+"\n")


def procuraItem(nome):
    index=0
    flag=0
    arquivo = open("produtos.txt", "r") 
    for line in arquivo:
        index +=1
        if nome == eval(line)['nome']:
            chave = index
            flag =1
    if flag == 0:
        arquivo.close()
        return 0
    else:
        arquivo.close()
        return chave  

def apagarProduto(findProduto):
        #Lista onde vão ser colocados os produtos dentro do arquivo
        #   V
        lista = []

        #Pega cada linha dentro do arquivo e joga dentro da lista
        #   V
        with open('produtos.txt', 'r') as arquivo:
            for numero, linha in enumerate(arquivo): #lê linha por linha o arquivo
                relatorio = eval(linha) #converte a linha do arquivo para dicionário
                lista.append(relatorio) #joga esse dicionário para dentro da lista

        #Deleta o produto dentro da lista
        #   V
        for x in range(0, len(lista)): #lê a lista de produtos indice por indice...
            if findProduto == lista[x]['nome']: #se o nome escrito do input for o mesmo do produto da lista, executa o comando

                del lista[x] #deleta o produto dentro da lista
                break #quebra o loop (evita o erro "index out of range")
        
        #Reescreve o arquivo com os produtos da lista
        #   V
        with open('produtos.txt', 'w') as arquivo: #Na hora de executar o comando, ele limpa o arquivo de texto para substituir os dados
            for x in range(0, len(lista)): #Lê a lista indice por indice
                arquivo.write(str(lista[x])+'\n') #Repõe os produtos da lista para dentro do arquivo de texto

def venda(nome,quant):
    chave=procuraItem(nome)
    temp={}
    if chave != False:
        try:
            with open('produtos.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                
          
                # pointer for position
                ptr = 1
                
                # opening in writing mode
                with open('produtos.txt', 'w') as fw:
                    for line in lines:
                        
                        # we want to remove 5th line
                        if ptr != chave:
                            fw.write(line)
                        else:
                            dif = eval(line)['quantidade'] -quant

                            temp=eval(line)
                            
                            
                            temp['quantidade'] = dif
                            lucro=quant*eval(line)['preco']
                            
                            with open('vendas.txt', 'a') as fv:
                                fv.write("item:{} lucro:{} quantidade vendida:{}\n".format(eval(line)['nome'],lucro,quant))
                            
                        ptr = ptr+1
                
        except:
            print("Oops! someting error")
        with open('produtos.txt', 'a') as fd:
            fd.write(str(temp)+'\n')
    else:
        print("NAO ENCONTRADO")

def relatorio():
    with open('vendas.txt','r') as arquivo:  
        print(arquivo.read())


def aumentarEstoque(estoque,quant):
    chave=procuraItem(estoque)
    temp={}
    if chave != False:
        
        
        try:
            with open('produtos.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
          
                # pointer for position
                ptr = 1
                
                # opening in writing mode
                with open('produtos.txt', 'w') as fw:
                    for line in lines:
                        
                      
                        if ptr != chave:
                            fw.write(line)
                        else:
                            dif = eval(line)['quantidade'] + quant

                            temp=eval(line)
                            
                            
                            temp['quantidade'] = dif
                            
                            
                            
                            
                        ptr = ptr+1
                
        except:
            print("Oops! someting error")
        with open('produtos.txt', 'a') as fd:
            fd.write(str(temp)+'\n')
    else:
        print("NAO ENCONTRADO")
