'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro
'''

numero = input('Digite um número para saber se é par ou impar: ')
eh_inteiro = numero.isdecimal()


if eh_inteiro:
    numero = int(numero)
    resto = numero % 2
    if resto == 0:
        print('Esse número é par')
    else:
        print('Esse número é impar')
else:
    print('Esse número não é inteiro')

