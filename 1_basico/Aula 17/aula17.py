'''
while em python
utilizado para realizar ações enquanto uma condição for verdadeira.

Requisitos: Entender condições e operadores.
'''

# while True:
#     nome = input('Qual é o seu nome? ')
#     print(f'Olá {nome}!')

# x = 0
# while x <=  100:
#     if x == 3:
#         x = x+1
#         break   #utilizado para quebrar o codigo, ao ver a palavra break, ele quebra o looping e vai para o final do codigo
#
#         #continue  - #utilizado para parar o codigo. Nesse caso, encontra-se pulando o número 3
#         #toda vez que ele encontra a palavra continue, ele não executa as linhas posteriores a palavra
#
#     print(x)
#     x = x + 1
#
# print('Acabou!')

x = 0 #coluna

# while x < 10:
#
#     y = 0  # linha
#
#     while y < 5:
#         print(f' ({x}, {y})')
#         y += 1
#     # print(x)
#     x+= 1 # x=x+1
#
# print('Acabou')

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Você deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1= int(num_1)
    num_2= int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido!')

