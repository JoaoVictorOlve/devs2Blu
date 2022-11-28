def contador(numInic, numFin, contagem):
    poli = '='*50

    print(poli)

    for x in range(1, 11):
        print(x)
    print(poli)

    for x in range(10, -2, -2):
        print(x)
    print(poli)

    #for x in range(numInic, numFin +1 if numFin > numInic else numFin -1, contagem):
    #    print(x)

    for x in range(numInic, numFin +1 if numFin > numInic else numFin -1, contagem):
        print(x)


inicio = int(input('Digite seu número inicial: '))
fim = int(input('Digite seu número final: '))
contagem = int(input('Digite sua contagem: '))

contador(inicio, fim, contagem)