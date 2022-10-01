'''
Operadores Lógicos
and, or, not
in e not in
'''

#o and compara entre 2 coisas
#comparacao1 and comparacao2

idade = int(input('Qual sua idade? '))
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'Pode pegar o empréstimo')
else:
    print(f'Não pode pegar o emprestimo')

# o or é comparação entre dois, tendo uma escolha. Um ou outra.
#comp1 or comp2

#O NOT inverte o valor - se não
'''
a = ''
b = 0

if not a:
    print('Por favor, preencha o valor de A')
'''
'''
#in
nome = 'Patricia'

if 'a' in nome:
    print('Existe A no seu nome')

# not in = ao contrário

if 'b' not in nome:
    print('Não existe')
'''