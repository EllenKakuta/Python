#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE 7 PESSOAS. NO FINAL MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES- considerar como maioridade 21 anos

import datetime
maiores=0
menores=0
for c in range(1,8):
    anoNascimento = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = datetime.date.today().year - anoNascimento
    if idade >= 21:
        maiores+=1
        print('Essa pessoa tem {} anos'.format(idade))
    else:
        menores+=1
        print('Essa pessoa tem {} anos'.format(idade))
print('-> {} pessoas já atingiram a maioridade de 21 anos'.format(maiores))
print('-> {} pessoas ainda não atingiram a maioridade de 21 anos'.format(menores))