'''
For / Else  em Python
'''

variavel = ['Patrícia Carvalho', 'Roberto Camargo', 'Steve', 'Gamora']

# for valor in variavel:
#     if valor.startswith('G'):   #startswith é para ver se a str começa com a letra escolhida
#         print('Começa com G', valor)
#     else:
#         print('Não começa com G', valor)

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):#lower converte a levra parea minuscula, assim consegue achar Maiusucla e Minuscula.
        comeca_com_j = True

    if comeca_com_j:
        print('Existe uma palavra que começa com J.')
    else:
        print('Não existe uma palavra com J.')

