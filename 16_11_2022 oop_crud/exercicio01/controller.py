def create(conta):
    contas = open('contas.py', 'a')
    contas.write(str(conta)+'\n')
    contas.close()