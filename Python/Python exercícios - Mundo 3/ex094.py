#CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL MOSTRE:
#A) QUANTAS PESSOAS FORAM CADASTRADAS
#B) A MÉDIA DE IDADE DO GRUPO
#C) UMA LISTA COM TODAS AS MULHERES
#D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA

pessoa={}
pessoas=[]
while True:
    pessoa['nome']=str(input(f'Nome: ')).title()
    while True:
        pessoa['sexo']=str(input(f'Sexo: [M/F] ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print(f'ERRO! Digite M ou F')
    pessoa['idade']=int(input(f'Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        continua=str(input('Quer continuar? [S/N] ')).upper()
        if continua in 'SN':
            break
        else:
            print('ERRO! Digite S ou N')
    if continua =='N':
        break
# print(pessoas) - teste
print(f'O grupo tem {len(pessoas)} pessoas cadastradas.')
soma_idade=0
mulheres=[]
acima_media=[]
# print(f'As mulheres cadastradas foram: ', end='') - CORREÇÃO NA AULA
for pessoa in pessoas:
    soma_idade+=pessoa['idade']
    media=soma_idade/len(pessoas)  
    if pessoa['sexo']=='F':
        mulheres.append(pessoa['nome'])
        # print(f'{pessoa["nome"]}', end='') - CORREÇÃO NA AULA
media=soma_idade/len(pessoas)  
print(f'A média de idade é {media:.2f} anos')
print(f'As mulheres cadastradas foram {mulheres}')
print(f'Lista das pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['idade']>=media:
        acima_media.append(pessoa.copy())        
for p in acima_media:
    print(f'Nome: {p['nome']}, sexo: {p['sexo']}, idade: {p['idade']}')

# for p in pessoas: - CORREÇÃO NA AULA
#     if p['idade']>=media:
#         print('   ')
#         for k,v in p.items():
#             print(f'{k} = {v}', end='')
#         print()

