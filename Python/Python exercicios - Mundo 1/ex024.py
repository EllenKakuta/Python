cidade = str(input('Digite o nome de uma cidade: ')).strip()#remover espaço em branco no início e no final da frase

print('A cidade digitada começa com a palavra Santo: {}'.format(cidade.upper().startswith('SANTO')))
print(cidade[:5].upper()=='SANTO') #FORMA ALTERNATIVA