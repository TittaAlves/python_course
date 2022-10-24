'''
 FOrmatação de Strings
 '''

nome = 'Patrícia'
print(nome)

idade = 25
altura = 1.55
e_maior = idade > 18
peso = 90
imc = (peso / (altura * altura))  # poderia usar: (peso / altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
