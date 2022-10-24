usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd= 'titta'
senha_bd= '12345'

if usuario_bd== usuario and senha_bd == senha:
    print('Você entrou no sistema')

else:
    print('Usuário ou senha inválido')