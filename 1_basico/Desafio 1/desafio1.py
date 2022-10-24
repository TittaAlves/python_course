'''
Criar variáveis para nome (str), idade (int)
altura (float) e peso (float) de uma pessoa
criar variável com o ano atual
obter o ano de nascimento da pessoa
obter o IMC da pessoa com 2 casas decimais
exibir um texto com todos os valores na tela usando f-strings
'''

nome= 'Patrícia Carvalho'
idade= 25
altura= 1.55
peso= 90
ano_atual= 2022
ano_nasc= (ano_atual - idade)
imc= (peso / altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')