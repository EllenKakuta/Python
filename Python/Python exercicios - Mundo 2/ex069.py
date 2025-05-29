#CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR. NO FINAL, MOSTRE:
#A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS
#B) QUANTOS HOMENS FORAM CADASTRADOS
#C)QUANTAS MULHERES TEM MENOS DE 20 ANOS

homem=maior_dezoito=menor_vinte=0
while True:
    print('- CADASTRO DE PESSOAS -')
    idade=int(input('Insira a idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Qual o sexo? [F/M]: ')).upper().strip()[0]
    if idade>=18:
        maior_dezoito+=1
    if sexo =='F' and idade <20:
       menor_vinte+=1
    if sexo=='M':
        homem+=1
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Deseja realizar novo cadastro? [S/N]: ')).upper().strip()[0]
    if resposta =='N':
        break
print(f'{maior_dezoito} pessoas tem mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{menor_vinte} mulheres tem menos de 20 anos')

