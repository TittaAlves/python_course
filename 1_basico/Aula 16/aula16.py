'''
Manipulando strings

* String indices
*Fatiamento de strings [inicio:fim:passo]
*Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

'''

#positivos  [012345678]
texto = 'Python s2'
print(texto[2])
# para pegar apenas o indice, uma lebra da frase, utilizado [2], com o número correspondente a letra.

nova_strings = texto[2:6]
#consigo definir o que quero que retorne, por exemplo quero do caracter 2 ao 6 "Thon" na tela.
#1 número inicio, último número fim, lembrando que o último nunca é representado, então se quero caractere 5, preciso por até o 6
#Se quiser do primeiro caracter e escolher onde termina, posso apenas por o final [:6] e também posso inverter, pegar do meio
#e pedir para ir até o final, exemplo [7:]
#Caso queira que ele pule os caracteres posso utilizar [0:6:2] ou [0: :3] - último é para indicar o quanto tem q pular


#negativos -[987654321]
#Basicamente a mesma coisa, por,e conta-se o número invertido
#Caso queira pegar a última letra, utiliza-se [-1], caso queria limitar [-9:-3] ou [-8:] ou [:-3]

print(nova_strings)
