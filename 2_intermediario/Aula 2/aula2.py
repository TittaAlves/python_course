'''
Funções (def) em Python - return - Part 2
'''


# nome = input('Qual o seu nome?')
#
#
# def exibe_msg(str, exibe_head):
#     if exibe_head:
#         print('#### Bem vindo ####')
#     str = str.strip()
#     print(f'O nome do usuário é {str}')
#     print(f'{str.upper()} você tem saldo na conta')
#
# exibe_msg(nome, False)
# exibe_msg(nome, False)
# exibe_msg(nome, True)
# exibe_msg(nome, False)

# variavel = funcao(f'O nome do usuário é {nome2}')

# if variavel:
#     print(variavel)
# else:
#     print('Nenhum Valor')

def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 /n2

divide = divisao(8,5)

if divide:
    print(divide)
else:
    print('Conta inválida')
