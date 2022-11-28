def calculoMedia(media1, media2, media3):
    print('Primeira nota:', media1)
    print('Segunda nota:', media2)
    print('Terceira nota:', media3)

    mediaFinal = (media1 + media2 + media3) / 3

    print('Média final: ', mediaFinal)

    if mediaFinal > 5:
        print('Aprovado!')
    else:
        print('Reprovado!')


media1 = int(input('Digite sua primeira nota: '))
media2 = int(input('Digite sua segunda nota: '))
media3 = int(input('Digite sua terceira nota: '))

calculoMedia(media1,media2,media3)