'''
Split, Join, Enumerate em Python
*Split - dividir um string #str
*Join - juntar uma lista #str
*Enumerate - enumerar elementos da lista #list
- aula 41
'''

# string = 'O Brasil é o país do futebol, o Brail é penta.'
# lista = string.split(' ')
# lista_2= string.split(',')

# print(lista)

# for valor in lista:
#     print(valor)


# for valor in lista:
#     print(f' A palavra {valor} apareceu {lista.count(valor)} x na frase.')

# palavra = ''
# contagem = 0
#
# for valor in lista:
#     qtd_vezes = lista.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem} x)')

# for valor in lista_2:
#     print(valor.strip().capitalize())

# string = 'O Brasil é penta'
# lista= string.split(' ')
# # string2= ','.join(lista)
# #
# # print(string)
# # print(lista)
# # print(string2)
#
# for v1, v2 in enumerate(lista):
#     print(v1, v2, lista[v1])

lista = ['Patricia', 'Roberto', 'Steve', 'Gamora']

for indice, nome in enumerate(lista):
    print(indice, nome)

# proxima aula 42
