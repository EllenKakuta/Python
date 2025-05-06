nome = str(input('Digite seu nome completo: '))

print('Nome com letras maiúsculas: {}'.format(nome.upper()))
print('Nome com letras minúsculas: {}'.format(nome.lower()))
print(len(nome))
separador = nome.split()
unidificador = ''.join(separador)
print('O total de letras é: {}'.format(len(unidificador)))
print('Seu primeiro nome tem {} letras'.format(len(separador[0])))

#-----------------------------------------------------------------#
nome = str(input('Digite seu nome completo: ')).strip() #Tira os espaços iniciais e finais
print(len(nome))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #outra forma de eliminar os espaços no meio das palavras