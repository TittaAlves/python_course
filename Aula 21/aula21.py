'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

# texto = 'Valor'
# lista = [1, 2, 3, 4, 'Patricia']

#         0    1    2    3   4
lista = ['A', 'B', 'C', 'D' 'E']
#    -    5    4    3    2    1
#
# string = 'ABCDE'
# print(lista[1])

# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1 + l2
# l4 = [1,2,3,4,5,6,7,8]
#
# l1.extend('a')  #utilizado para add algo a uma lista já criada
#
# l2.append('b')  #adiciona um valor na lista
#
# l2.insert(0, 'ba')  #aqui posso escolher onde adicionar, começo, meio ou fim
#
# l2.pop() #aqui excluo o último valor
#
# del(l2[1:3])  #aqui posso exlcuir Qual indice excluir
#
# print( max(l4) )  #aqui mostro o indice maior
# print( min(l4) )  #aqui mostra o indice menor
#
#
#
# print(l1)
# print(l2)
# print(l3)


# l2 = list(range(1,10))  #a função range não nós trás uma lista
# # por isso eu posso e devo utilizar a função list na frente para converter em lista
# print(l2)


secreto = 'pulseira'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh, isso não vale. Digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'EBAA, a letra "{letra}" existe na palavra secreta')

    else:
        print(f'AFFF, a letra "{letra}" NÃO existe na palavra secreta')
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



