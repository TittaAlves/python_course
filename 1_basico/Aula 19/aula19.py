#   Índices
#   0123456789........................33
# Iterando strings com whilw em Python


frase = 'O rato roeu a roupa do rei de roma'  #chamado de iterável
tamanho_frase =len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula? ')

# while contador < tamanho_frase:
#     #print(frase[contador], contador)
#     #nova_string += frase[contador]
#     letra = frase[contador]
#     if letra == 'r':
#         nova_string += 'R'
#     else:
#         nova_string += letra
#     contador += 1
#
# print(nova_string)


# iteração <- iterar
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()  # .upper() - para colocar as letras em maiúscula
    else:
        nova_string += letra
    contador += 1

print(nova_string)
