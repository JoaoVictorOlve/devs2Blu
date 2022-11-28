from controller import cadastroProduto,venda,apagarProduto,relatorio,aumentarEstoque

def menu():


    menu = 1
    while (menu!=0):
            print('='*30, 'CATARININHO MEGA STORE', '='*30)

            print('\n O que podemos fazer para você hoje?\n')

            menu = int(input('1. -> Cadastro de Produto\n2. -> Relatorio de Vendas\n3. -> Venda\n4. -> Apagar Produto\n5. -> Aumentar Estoque\n0. -> Sair\n>: '))

            match menu:
                case 1:

                    produto = {} 
                    quantidadeInicial={}
                    produto['nome']=str(input("Digite o nome do produto: "))   
                    produto['tipo']=str(input("Digite o tipo do produto: "))
                    produto['preco']=float(input("Insira o preço do seu produto: "))
                    produto['quantidade']=int(input("Digite a quantidade de itens: "))
                    produto['quantidadeInicial']=produto['quantidade']
                    cadastroProduto(produto)
                case 2:
                    relatorio()
                case 3:
                    nome=str(input("digite o nome do item vendido"))
                    quant=int(input("digite a quantidade vendida: "))
                    venda(nome,quant)
                case 4:
                    produto = input('Informe o produto: ')
                    apagarProduto(produto)
                case 5:
                    estoque = str(input('Informe o nome do produto que queira aumentar o estoque\n>'))
                    quant=int(input("digite a quantidade aumentada: "))
                    aumentarEstoque(estoque,quant)
                
        


menu()
