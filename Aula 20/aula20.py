'''
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
'''

texto = 'Python'
nova_string = ''

#continue - pula pala o proxiomo laço
#break - termina o laço


for letra in texto:
    if letra == 't':
        #continue - aqui ele pula o T e continua após
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        #break aqui ele poem a letra H porém quebra tudo após
    else: nova_string += letra

print(nova_string)


# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# for letra in texto:
#     print(letra)

# for n in range(0, 10, 2):
#     print(n)
#
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

