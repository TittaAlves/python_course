secreto = 'python'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print(f'Você perdeu! A palavra secreta era {secreto}')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh, isso não vale. Digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'EBAA, a letra "{letra}" existe na palavra secreta')

    else:
        print(f'Que pena, a letra "{letra}" NÃO existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, Você GANHOU! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print (f'Você ainda tem {chances} chances.')

