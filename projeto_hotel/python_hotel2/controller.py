import os


def fazerCheckin(cliente):
    with open('hotel.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+"\n")

        
def relatorioHospedes():
    with open('hotel.txt') as arquivo:
        print("\n*** Lista de Hospedes ***\n")
        for numero, linha in enumerate(arquivo):
            relatorio = linha.replace("{'nome':","Nome:").replace("'","").replace("sobrenome:","| Sobrenome:").replace("idade:","| Idade:").replace("}","").replace(",", "")
            print(f"{numero} -", relatorio)

'''def listarHospede():
    with open('hospedes.txt') as arquivo:
        print("\n*** Lista de Hospedes ***\n")
        for numero, linha in enumerate(arquivo):
            relatorio = linha.replace("{'nome':","Nome:").replace("'","").replace("telefone:","Telefone:").replace("cpf:","CPF:").replace("}","")
            print(f"{numero + 1} -", relatorio)'''



def procurarHospedes(clienteFind):
    index=0
    flag=0
    arquivo = open('hotel.txt') 
    for line in arquivo:
        index +=1
        if clienteFind == ['nome']:
            print(line)
            flag =1
    if flag == 0:
        print("Cliente não encontrado")
        
        

def fazerCheckout(clienteFind):
    index=0
    flag=0
    arquivo = open("hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if clienteFind == ['nome']:
            chave = index
            flag =1
    arquivo.close()
    if flag == 0:
        print("Cliente não encontrado")
    
    else:
        try:
            with open('python_hotel/hotel.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                
          
                # pointer for position
                ptr = 1
      
                # opening in writing mode
                with open('hotel.txt', 'w') as fw:
                    for line in lines:
                
                        # we want to remove 5th line
                        if ptr != chave:
                            fw.write(line)
                        ptr += 1
            print("Deleted")
      
        except:
            print("Oops! someting error")