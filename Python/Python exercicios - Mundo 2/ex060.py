#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE SEU FATORIAL
#EX: 5!=5x4x3x2x1=120
fatorial = 1
print('FATORIAL DO NÚMERO')
numero=int(input('Digite o número para que eu te dê o resultado: '))
contador = numero
while contador>0: #enquanto o contador for maior que zero, haverá a multiplicação do fatorial pelo contador e a cada loop, diminui a até zerar
    fatorial*=contador
    contador -=1
print('{}! = {}'.format(numero,fatorial))


'''
outra forma de fazer:

n=int(input('Digite um número para calcular o fatorial: '))
c=n
f=1
print('Calculando {}! = '.format(n), end='')
while c>0:
    print('{} '.format(c),end=' ')
    print(' x ' if c>1 else ' = ', end=' ')
    f*+c
    c-=1 -->para aparescer o número descrescente
print('{}'.format(f))
'''