'''
While / Else

contadores
acumuladores
'''

contador = 1
acumulador = 1

while contador <= 100:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei ao final!')

    #se colocar o print fora do else, caso quebre o codigo em um momento, ele ainda aprecerá na tela.
    #Caso tenha colocado no else, o else não aparecerá.


