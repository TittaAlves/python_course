'''
Tipos de dados
str- string (textos 'assim' ou "assim")
int- inteiro (123456 0  -10  -500)
float- real/ ponto flutuante (número positivo ou negativo com ponto 0,0  1,0  10,50)
bool -booleano/lógico  (true /  false)
'''


print(type('Patrícia'))  #type, me trás o valor do dado
print(type(12345))
print(type(25.23))
print(type(10==10))

print('Patrícia', type('Patrícia'))
print(10, type(10))
print(25.23, type(25.23))
print(10==10, type(10==10))

print('10', type('Patrícia'), type(int('10')))

#Exercício
#String: nome
print('Patrícia Carvalho', type ('Patricia Carvalho'))

#Int: idade
print(25, type(25))

#Float: altura
print(1.55, type(1.55))

#Bool: É maior de idade?
print(25 > 18, type(25 > 18))
