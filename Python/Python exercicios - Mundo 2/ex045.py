#CRIAR PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM O USUÁRIO

import random

print('****** J O K E N P Ô ******')
usuario = int(input('Escolha una das opções abaixo: \n' \
'1- PEDRA \n' \
'2- PAPEL \n' \
'3- TESOURA \n' \
'-> '))
lista = [1,2,3]
computador = random.choice(lista)
if usuario ==1 and computador == 1:
    print('Você: Pedra')
    print('Computador: Pedra')
    print('EMPATE')
elif usuario ==1 and computador ==2:
    print('Você: Pedra')
    print('Computador: Papel')
    print('VOCÊ PERDEU!')
elif usuario ==1 and computador ==3:
    print('Você: Pedra')
    print('Computador: Tesoura')
    print('VOCÊ GANHOU!')
    print('PARABÉNS!')
elif usuario ==2 and computador ==1:
    print('Você: Papel')
    print('Computador: Pedra')
    print('VOCÊ GANHOU!')
    print('PARABÉNS!')
elif usuario == 2 and computador ==2:
    print('Você: Papel')
    print('Computador: Papel')
    print('EMPATE')
elif usuario == 2 and computador ==3:
    print('Você: Papel')
    print('Computador: Tesoura')
    print('VOCÊ PERDEU!')
elif usuario ==3 and computador ==1:
    print('Você: Tesoura')
    print('Computador: Pedra')
    print('VOCÊ PERDEU!')
elif usuario ==3 and computador ==2:
    print('Você: Tesoura')
    print('Computador: Papel')
    print('VOCÊ GANHOU!')
    print('PARABÉNS!')
elif usuario ==3 and computador ==3:
    print('Você: Tesoura')
    print('Computador: Tesoura')
    print('EMPATE')
else:
    print('Opção inválida!')