'''
Faça um programa que pergunte a hora ao usúario e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex:
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23
'''

hora= input('Que horas são? ')
eh_inteiro = hora.isdecimal()

if eh_inteiro:
    hora = int(hora)
    if hora >= 1 and hora <= 12:
        print('Bom dia!')

    elif hora >= 13 and hora <= 17:
        print('Boa tarde!')

    elif hora >= 18:
        print('Boa noite!')

else:
    print('Digite apenas números')

