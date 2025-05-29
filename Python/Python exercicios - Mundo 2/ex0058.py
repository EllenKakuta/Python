#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.

import random
import time
computador =(random.randint(0,10))
numero=0
# print (computador)
palpite=0
print('EM QUE NÚMERO ESTOU PENSANDO?')
time.sleep(1)
while numero != computador:
    numero = int(input('Digite um número entre 0 e 10: '))
    if numero>10:
        print('Valor inválido!')
    if numero < computador:
        print('Mais.. tente outra vez..')
    elif numero > computador:
        print('Menos.. tente outra vez..')
    palpite +=1
time.sleep(0.5)
if palpite !=1:
    print('UFFAAAA!')
    time.sleep(1)    
    print('Após {} tentativas, você acertou!'.format(palpite))
else:
    print('PARABÉNS! VOCÊ ACERTOU!')