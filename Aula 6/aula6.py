'''
Iniciar com letra, pode conter números, separar _, letras minúsculas
'''

nome = 'Patrícia'
print(nome)

idade = 25
altura = 1.55
e_maior = idade > 18
peso = 90
imc = (peso / (altura * altura))  # poderia usar: (peso / altura ** 2)

print('Nome:', nome)
print('Idade', idade)
print('Altura:', altura)
print('É maior: ', e_maior)

print(idade * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
