nome = str(input('Digite seu nome completo: ')).strip()
divisor = nome.split()
print('Seu primeiro nome é: {}'.format(divisor[0]))

# print('Seu último nome é: {}'.format(nome.rsplit(" ",1)[1]))
print('Seu último nome é: {}'.format(divisor[len(divisor)-1])) #posição de nome tamanho -1