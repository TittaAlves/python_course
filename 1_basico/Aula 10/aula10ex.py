#Atividade

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#Limite para pegar empréstimo > 18 anos
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo')

else:
    print(f'{nome} NÃO PODE pegar o empréstimo')