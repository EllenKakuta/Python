#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES(DESCONSIDERANDO O FLAG)


soma=0
contador=0
while True:
    numero=int(input('Digite um número qualquer [999 ENCERRARÁ O PROGRAMA]: '))
    if numero ==999:
        break
    soma+=numero
    contador+=1
print(f'Foram digitados {contador} números e a soma entre eles é: {soma}')