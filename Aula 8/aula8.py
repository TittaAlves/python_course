'''
Entrada de dados

input- para enviar uma pergunta
'''

nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')
peso = input('Qual seu peso? ')
altura = input('Qual sua altura? ')
IMC = int(peso) / float(altura) ** 2
ano_nascimento= 2022-int(idade)

print(f'O usuário se chama: {nome} e tem {idade} anos de idade e nasceu em {ano_nascimento}')
print(f'Sua altura é {altura} e seu peso {peso}kg sendo assim, seu IMC é de {IMC:.2f}')


