cidade = str(input('Digite o nome de uma cidade: ')).strip()

print('A cidade digitada começa com a palavra Santo: {}'.format(cidade.upper().startswith('SANTO')))
print(cidade[:5].upper()=='SANTO') #FORMA ALTERNATIVA