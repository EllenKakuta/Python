#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES(DESCONSIDERANDO O FLAG(999))

contador=0
soma=0
numero=0
print('LEITOR DE NÚMEROS - O NÚMERO 999 ENCERRARÁ O PROGRAMA')
while numero !=999:
    numero=int(input('Digite um número qualquer: '))
    if numero !=999:
        soma+=numero
        contador+=1
print('Ao todo, foram digitados: {} números'.format(contador))
print('A soma entre os números digitados é: {}'.format(soma))