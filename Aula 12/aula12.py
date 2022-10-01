# Quantidade de caracteres str
#len - contar quantidade   - não utiliza-se em bool, int, float

usuario= input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

#print(usuario, qtd_caracteres,type(qtd_caracteres))

'''
if qtd_caracteres < 6:
    print('Quantidade inadequada')
else:
    print('Você foi cadastrado')
'''

string1= input('Digite algo')
string2= input('Digite outra coisa')

print(f'Aquantidade de caracteres digitados foi {len(string1) + len(string2)}')

