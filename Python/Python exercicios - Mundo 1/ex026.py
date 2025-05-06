frase = str(input('Escreva uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase digitada'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(frase.upper().find('A')+1))
print('A letra "A" aparece pela útilma vez na posição: {}'.format(frase.upper().rfind('A')+1))
