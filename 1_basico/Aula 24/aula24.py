'''
Desempacotamento de listas em Python
'''

lista = ['Patrícia', 'Roberto', 'Gamora', 'Steve', 1, 2 ,3]

n1, n2, n3, n4, *outra_lista = lista

print(n2, outra_lista)