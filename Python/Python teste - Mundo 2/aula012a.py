nome= str(input('Qual é o seu nome? '))
if nome == 'Ellen':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
# else: #---> PODE SER USADO TBM SEM O ELSE
#     print('Seu nome é bem normal..') 
print('Tenha um bom dia, {}!'.format(nome))