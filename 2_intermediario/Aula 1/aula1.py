'''
Funções - def em Python (parte 1)
'''

def funcao ():
    print('Olá Mundo!')

funcao ()

def funcao(msg='Ola', nome='usuário'):
    nome= nome.replace('e', '3')
    returne f'{msg}, {nome}'

funcao(nome='Patricia')
funcao('Oi', 'Roberto')